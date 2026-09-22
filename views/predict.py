import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from utils import load_model_bundle, RATING_LABELS, ARABIC_LABELS

bundle = load_model_bundle()
model = bundle["model"]
encoders = bundle["encoders"]
scaler = bundle["scaler"]
target_encoder = bundle["target_encoder"]
feature_columns = bundle["feature_columns"]
cat_cols = bundle["cat_cols"]
num_cols = bundle["num_cols"]

RATING_COLS = [c for c in num_cols if c != "Flight_Distance"]

st.markdown("""
<div class="hero">
    <h1>🔮 Passenger Satisfaction Prediction</h1>
    <p>Enter a hypothetical passenger's information and service ratings to receive an instant prediction of their satisfaction with the flight.</p>
</div>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1.3], gap="large")

with col_left:
    st.markdown('<div class="card"><h4>Passenger & Flight Information</h4>', unsafe_allow_html=True)
    gender = st.radio("Gender", encoders["Gender"].classes_, horizontal=True)
    customer_type = st.radio("Customer Type", encoders["Customer_Type"].classes_, horizontal=True)
    travel_type = st.radio("Travel Type", encoders["Type_of_Travel"].classes_, horizontal=True)
    travel_class = st.selectbox("Class", encoders["Class"].classes_)
    flight_distance = st.slider("Flight Distance (miles)", 31, 3739, 800)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="card"><h4>Service Ratings (0 = Not Applicable · 5 = Excellent)</h4>', unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    ratings = {}
    for i, col in enumerate(RATING_COLS):
        target_col = r1 if i % 2 == 0 else r2
        with target_col:
            ratings[col] = st.slider(RATING_LABELS.get(col, col), 0, 5, 3, key=col)
    st.markdown('</div>', unsafe_allow_html=True)

predict_clicked = st.button("🔮  Predict Passenger Satisfaction", use_container_width=True)

if predict_clicked:
    row = {
        "Gender": gender,
        "Customer_Type": customer_type,
        "Type_of_Travel": travel_type,
        "Class": travel_class,
        "Flight_Distance": flight_distance,
    }
    row.update(ratings)
    input_df = pd.DataFrame([row])[feature_columns]

    for col in cat_cols:
        input_df[col] = encoders[col].transform(input_df[col])
    input_df[num_cols] = scaler.transform(input_df[num_cols])

    proba = model.predict_proba(input_df)[0]
    pred_idx = int(np.argmax(proba))
    pred_label = target_encoder.classes_[pred_idx]
    confidence = proba[pred_idx] * 100
    satisfied_prob = proba[list(target_encoder.classes_).index("satisfied")] * 100

    is_satisfied = pred_label == "satisfied"
    box_class = "result-satisfied" if is_satisfied else "result-dissatisfied"
    emoji = "😊" if is_satisfied else "😕"
    headline = "Satisfied" if is_satisfied else "Neutral / Dissatisfied"

    res_col, gauge_col = st.columns([1, 1], gap="large")
    with res_col:
        st.markdown(f"""
        <div class="result-box {box_class}">
            <div style="font-size:2.6rem;">{emoji}</div>
            <h2>{headline}</h2>
            <p style="color:#b8c4d9; font-size:1rem;">Model Confidence: <b>{confidence:.1f}%</b></p>
        </div>
        """, unsafe_allow_html=True)

    with gauge_col:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=satisfied_prob,
            number={'suffix': "%", 'font': {'color': '#f5f7fb'}},
            title={'text': "Satisfaction Probability", 'font': {'color': '#9fb0c9', 'size': 14}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': '#9fb0c9'},
                'bar': {'color': "#f4b942"},
                'bgcolor': "rgba(0,0,0,0)",
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(244,90,66,0.25)'},
                    {'range': [40, 70], 'color': 'rgba(244,180,66,0.2)'},
                    {'range': [70, 100], 'color': 'rgba(66,244,127,0.25)'},
                ],
            }
        ))
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", font_color="#e8ecf4",
            height=250, margin=dict(l=20, r=20, t=50, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)

st.markdown('<div class="card"><h4>What Influences the Model\'s Decision?</h4>', unsafe_allow_html=True)
importances = pd.Series(model.feature_importances_, index=feature_columns).sort_values(ascending=True)
ar_index = [ARABIC_LABELS.get(i, i) for i in importances.index]
fig_imp = px.bar(
    x=importances.values, y=ar_index, orientation="h",
    labels={"x": "Relative Importance", "y": ""},
    color=importances.values, color_continuous_scale=["#14213d", "#f4b942"],
)
fig_imp.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font_color="#e8ecf4", showlegend=False, coloraxis_showscale=False,
    height=440, margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig_imp, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)