import streamlit as st

from utils import inject_theme

st.set_page_config(
    page_title="Flight Satisfaction Predictor",
    page_icon="🛫",
    layout="wide",
)

inject_theme()

pages = [
    st.Page("views/home.py", title="Home", icon="🏠", default=True),
    st.Page("views/eda.py", title="Exploratory Data Analysis", icon="📊"),
    st.Page("views/predict.py", title="Prediction", icon="🔮"),
]

pg = st.navigation(pages, position="sidebar")

pg.run()