import streamlit as st
from utils import load_model_bundle, load_eda_bundle

bundle = load_model_bundle()
eda = load_eda_bundle()

test_accuracy = bundle.get("test_accuracy", 0)
test_f1 = bundle.get("test_f1", 0)
n_train = eda.get("n_train", 0)

st.markdown(f"""
<div class="hero">
    <span class="badge">RANDOM FOREST</span>
    <span class="badge">{test_accuracy*100:.1f}% Accuracy</span>
    <span class="badge">{n_train:,} Training Rows</span>
    <h1>🛫 Flight Satisfaction Predictor</h1>
    <p>
    A machine learning project that predicts airline passenger satisfaction —
    <b>Satisfied</b> or <b>Neutral / Dissatisfied</b> —
    based on flight data and passenger ratings of various onboard services.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.3, 1], gap="large")

with col1:
    st.markdown("""
    <div class="card">
        <h4>🎯 Project Overview</h4>
        <p>
        The original dataset (<b>Airline Passenger Satisfaction</b>) contains survey responses
        from over 130,000 airline passengers. Each passenger rates various services such as
        Wi-Fi, food, seat comfort, entertainment, and crew service — and finally indicates
        whether they were satisfied with the flight.
        </p>
        <p>
        The goal of this project is to build a model that can predict passenger satisfaction
        before asking them directly, using flight information and service ratings.
        This can help airlines identify the factors that most affect passenger experience
        and focus their improvement efforts accordingly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>⚙️ Model Development Steps</h4>
        <p>1. <b>Data Cleaning:</b> Removing missing rows and duplicates.</p>
        <p>2. <b>Feature Selection:</b> After analyzing correlations, 6 columns with weak
        relationships to satisfaction were removed (such as age, gate location, and departure
        time convenience), leaving 16 features.</p>
        <p>3. <b>Encoding and Scaling:</b> Label Encoding for categorical columns (gender,
        customer type, travel type, and class), and Standard Scaling for numerical columns.</p>
        <p>4. <b>Training:</b> Several models were tested (Logistic Regression, SVM, KNN,
        Decision Tree, Random Forest, AdaBoost, Gradient Boosting, XGBoost, LightGBM, and
        CatBoost), with <b>Random Forest</b> selected as the best balance between performance
        and model size.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h4>📈 Model Performance</h4>', unsafe_allow_html=True)
    m1, m2 = st.columns(2)
    m1.metric("Test Accuracy", f"{test_accuracy*100:.1f}%")
    m2.metric("F1 Score", f"{test_f1:.3f}")
    st.markdown("""
    <p style="margin-top:0.8rem;">
    These metrics were calculated on an independent test set that was completely separate
    from the training data — meaning they reflect the model's performance on data it
    has never seen before.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🧭 How to Use the App</h4>
        <p>📊 <b>Data Analysis</b> — Explore the charts and statistics generated from the
        original dataset, and discover which factors are most strongly associated with
        passenger satisfaction.</p>
        <p>🔮 <b>Prediction</b> — Enter data for a hypothetical passenger (ratings + travel
        information) and receive an instant satisfaction prediction with a confidence score.</p>
    </div>
    """, unsafe_allow_html=True)