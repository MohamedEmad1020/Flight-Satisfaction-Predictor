import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from utils import load_eda_bundle, ARABIC_LABELS

eda = load_eda_bundle()
satisfaction_counts = eda["satisfaction_counts"]
cat_by_satisfaction = eda["cat_by_satisfaction"]
histograms = eda["histograms"]
corr_matrix = eda["corr_matrix"]
corr_with_target = eda["corr_with_target"]
cat_cols = eda["cat_cols"]

DARK_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#e8ecf4",
    legend=dict(bgcolor="rgba(0,0,0,0)"),
)
COLOR_SAT = "#f4b942"
COLOR_NEU = "#4a6fa5"

st.markdown("""
<div class="hero">
    <h1>📊 Exploratory Data Analysis (EDA)</h1>
    <p>Exploring the original dataset before training — satisfaction distribution, relationships
    between services and satisfaction, and the factors most strongly associated with passenger experience.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# 1. Overall satisfaction distribution
# ---------------------------------------------------------------------------
col1, col2 = st.columns([1, 1.4], gap="large")

with col1:
    st.markdown('<div class="card"><h4>Overall Satisfaction Distribution</h4>', unsafe_allow_html=True)
    labels = list(satisfaction_counts.keys())
    values = list(satisfaction_counts.values())
    total = sum(values)
    fig = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.55,
        marker=dict(colors=[COLOR_SAT if l == "satisfied" else COLOR_NEU for l in labels]),
        textinfo="percent+label",
    ))
    fig.update_layout(**DARK_LAYOUT, height=320, showlegend=False, margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(fig, use_container_width=True)
    pct_satisfied = satisfaction_counts.get("satisfied", 0) / total * 100
    st.markdown(f"""
    <div class="insight-box">
    Out of {total:,} passengers, only <b>{pct_satisfied:.1f}%</b> are satisfied with their flight —
    meaning the dataset is relatively balanced between the two classes, making it suitable
    for training without the need for additional balancing techniques (such as SMOTE).
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# 2. Correlation with satisfaction (bar chart) — matches notebook cell 20
# ---------------------------------------------------------------------------
with col2:
    st.markdown('<div class="card"><h4>Factors Most Strongly Correlated with Satisfaction</h4>', unsafe_allow_html=True)
    top_corr = corr_with_target.sort_values(ascending=True).tail(12)
    ar_labels = [ARABIC_LABELS.get(i, i) for i in top_corr.index]
    fig = px.bar(
        x=top_corr.values, y=ar_labels, orientation="h",
        color=top_corr.values, color_continuous_scale=["#14213d", "#f4b942"],
        labels={"x": "Correlation Strength", "y": ""},
    )
    fig.update_layout(**DARK_LAYOUT, height=380, coloraxis_showscale=False, margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
    <div class="insight-box">
    <b>Online boarding</b>, <b>Inflight entertainment</b>, and <b>Seat comfort</b> are the three
    factors most strongly correlated with passenger satisfaction — which is why the original
    notebook removed columns such as <b>Age</b> and <b>Gate location</b> from training due to
    their weak correlation.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# 3. Histograms by satisfaction for key numeric columns
# ---------------------------------------------------------------------------
st.markdown('<div class="card"><h4>Distribution of Key Features by Satisfaction</h4>', unsafe_allow_html=True)
hist_choice = st.selectbox(
    "Select a feature",
    options=list(histograms.keys()),
    format_func=lambda c: ARABIC_LABELS.get(c, c),
)
h = histograms[hist_choice]
edges = h["edges"]
centers = [(edges[i] + edges[i+1]) / 2 for i in range(len(edges) - 1)]

fig = go.Figure()
fig.add_trace(go.Bar(x=centers, y=h["satisfied"], name="Satisfied", marker_color=COLOR_SAT, opacity=0.85))
fig.add_trace(go.Bar(x=centers, y=h["neutral"], name="Neutral / Dissatisfied", marker_color=COLOR_NEU, opacity=0.85))
fig.update_layout(**DARK_LAYOUT, barmode="overlay", height=380,
                   xaxis_title=ARABIC_LABELS.get(hist_choice, hist_choice), yaxis_title="Number of Passengers",
                   margin=dict(t=20, b=10, l=10, r=10))
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# 4. Categorical breakdown
# ---------------------------------------------------------------------------
st.markdown('<div class="card"><h4>Satisfaction by Passenger Characteristics</h4>', unsafe_allow_html=True)
cat_tabs = st.tabs([ARABIC_LABELS.get(c, c) for c in cat_cols])
for tab, col in zip(cat_tabs, cat_cols):
    with tab:
        ct = cat_by_satisfaction[col]
        categories = list(next(iter(ct.values())).keys())
        fig = go.Figure()
        for satisfaction_label, color in [("satisfied", COLOR_SAT), ("neutral or dissatisfied", COLOR_NEU)]:
            vals = [ct[satisfaction_label][cat] for cat in categories]
            fig.add_trace(go.Bar(x=categories, y=vals, name=satisfaction_label, marker_color=color))
        fig.update_layout(**DARK_LAYOUT, barmode="group", height=340, margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# 5. Correlation heatmap
# ---------------------------------------------------------------------------
st.markdown('<div class="card"><h4>Complete Correlation Heatmap</h4>', unsafe_allow_html=True)
ar_cols = [ARABIC_LABELS.get(c, c) for c in corr_matrix.columns]
fig = go.Figure(go.Heatmap(
    z=corr_matrix.values, x=ar_cols, y=ar_cols,
    colorscale=[[0, "#4a6fa5"], [0.5, "#14213d"], [1, "#f4b942"]],
    zmin=-1, zmax=1,
))
fig.update_layout(**DARK_LAYOUT, height=560, margin=dict(t=10, b=10, l=10, r=10))
st.plotly_chart(fig, use_container_width=True)
st.markdown("""
<div class="insight-box">
Notice how service-related features (such as Cleanliness with Inflight service, or Seat comfort
with Food and drink) tend to move together strongly — this makes sense because a passenger
who is satisfied with one service will often be satisfied with other services as well.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)