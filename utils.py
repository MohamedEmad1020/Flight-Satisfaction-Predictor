import streamlit as st
import joblib

RATING_LABELS = {
    "Inflight_wifi_service": "📶 Inflight Wifi",
    "Food_and_drink": "🍽️ Food & Drink",
    "Online_boarding": "🎫 Online Boarding",
    "Seat_comfort": "💺 Seat Comfort",
    "Inflight_entertainment": "🎬 Inflight Entertainment",
    "On_board_service": "🧑‍✈️ On-board Service",
    "Leg_room_service": "🦵 Leg Room",
    "Baggage_handling": "🧳 Baggage Handling",
    "Checkin_service": "🖥️ Check-in Service",
    "Inflight_service": "🛎️ Inflight Service",
    "Cleanliness": "✨ Cleanliness",
}

ARABIC_LABELS = {
    "Flight_Distance": "Flight Distance",
    "Online_boarding": "Online Boarding",
    "Inflight_wifi_service": "Inflight Wifi Service",
    "Seat_comfort": "Seat Comfort",
    "Inflight_entertainment": "Inflight Entertainment",
    "Checkin_service": "Check-in Service",
    "Age": "Passenger Age",
    "Gender": "Gender",
    "Customer_Type": "Customer Type",
    "Type_of_Travel": "Travel Type",
    "Class": "Class",
    "On_board_service": "On-board Service",
    "Leg_room_service": "Leg Room Service",
    "Baggage_handling": "Baggage Handling",
    "Inflight_service": "Inflight Service",
    "Cleanliness": "Cleanliness",
    "Food_and_drink": "Food and Drink",
    "Ease_of_Online_booking": "Ease of Online Booking",
    "Departure_Delay_in_Minutes": "Departure Delay (Minutes)",
    "Arrival_Delay_in_Minutes": "Arrival Delay (Minutes)",
    "Departure_Arrival_time_convenient": "Departure/Arrival Time Convenience",
    "Gate_location": "Gate Location",
}


def inject_theme():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Tajawal:wght@400;500;700&display=swap');

        html, body, [class*="css"] { font-family: 'Space Grotesk', 'Tajawal', sans-serif; }

        .stApp {
            background: radial-gradient(circle at 15% 0%, #14213d 0%, #0a0e1a 45%, #05070d 100%);
            color: #e8ecf4;
        }

        #MainMenu, footer { visibility: hidden; }

        .hero {
            padding: 1.6rem 2rem;
            border-radius: 18px;
            background: linear-gradient(120deg, rgba(244,180,66,0.12), rgba(20,33,61,0.4));
            border: 1px solid rgba(244,180,66,0.25);
            margin-bottom: 1.4rem;
        }
        .hero h1 { font-size: 2rem; margin: 0; font-weight: 700; color: #f5f7fb; letter-spacing: -0.5px; }
        .hero p { color: #9fb0c9; margin: 0.35rem 0 0 0; font-size: 0.98rem; line-height: 1.6; }
        .badge {
            display: inline-block; padding: 3px 12px; border-radius: 999px;
            background: rgba(244,180,66,0.15); border: 1px solid rgba(244,180,66,0.4);
            color: #f4b942; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.5px;
            margin-right: 6px; margin-bottom: 6px;
        }

        .card {
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 1.3rem 1.4rem;
            margin-bottom: 1rem;
        }
        .card h4 {
            margin-top: 0; color: #f4b942; font-size: 0.95rem;
            text-transform: uppercase; letter-spacing: 1px; font-weight: 600;
        }
        .card p, .card li { color: #c7d1e3; line-height: 1.8; }

        .insight-box {
            background: rgba(244,180,66,0.08);
            border-right: 3px solid #f4b942;
            border-radius: 8px;
            padding: 0.7rem 1rem;
            margin-top: 0.6rem;
            color: #e8ecf4;
            font-size: 0.92rem;
        }

        div[data-testid="stMetric"] {
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px; padding: 0.8rem 1rem;
        }
        div[data-testid="stMetricValue"] { color: #f4b942; }

        .stButton > button {
            background: linear-gradient(120deg, #f4b942, #e08e2e);
            color: #14213d; font-weight: 700; border: none; border-radius: 12px;
            padding: 0.7rem 1.2rem; width: 100%; font-size: 1.02rem;
            transition: transform 0.15s ease;
        }
        .stButton > button:hover { transform: translateY(-1px); }

        .result-box {
            border-radius: 18px; padding: 1.6rem; text-align: center;
            margin-top: 0.6rem;
        }
        .result-satisfied { background: linear-gradient(120deg, rgba(66,244,127,0.14), rgba(20,33,61,0.3)); border: 1px solid rgba(66,244,127,0.4); }
        .result-dissatisfied { background: linear-gradient(120deg, rgba(244,90,66,0.14), rgba(20,33,61,0.3)); border: 1px solid rgba(244,90,66,0.4); }
        .result-box h2 { margin: 0.2rem 0; font-size: 1.6rem; }

        [data-testid="stSidebarNav"] { font-family: 'Space Grotesk', sans-serif; }
    </style>
    """, unsafe_allow_html=True)


@st.cache_resource
def load_model_bundle():
    return joblib.load("satisfaction_model.pkl")


@st.cache_resource
def load_eda_bundle():
    return joblib.load("eda_data.pkl")