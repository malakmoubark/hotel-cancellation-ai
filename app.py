import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(
    page_title="Hotel Cancellation AI",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(6,182,212,0.20), transparent 28%),
        radial-gradient(circle at 100% 0%, rgba(236,72,153,0.18), transparent 28%),
        radial-gradient(circle at 50% 100%, rgba(20,184,166,0.12), transparent 30%),
        linear-gradient(135deg, #07111f, #0b1728 45%, #111827);
}


section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #07111f 0%,
            #0b1f33 55%,
            #082f3d 100%
        );

    border-right: 1px solid rgba(45,212,191,0.18);
}

section[data-testid="stSidebar"] h2 {
    color: #67e8f9;
}

section[data-testid="stSidebar"] label {
    color: #dbeafe !important;
    font-weight: 600;
}


div[data-baseweb="select"] > div {
    background: rgba(15,23,42,0.85) !important;
    border: 1px solid rgba(45,212,191,0.35) !important;
    border-radius: 12px !important;
}

div[data-testid="stNumberInput"] input {
    background: rgba(15,23,42,0.85) !important;
    color: white !important;
    border: 1px solid rgba(45,212,191,0.30) !important;
}


.hero {
    position: relative;
    overflow: hidden;

    padding: 48px;
    margin-bottom: 32px;

    border-radius: 30px;

    background:
        linear-gradient(
            120deg,
            #083344 0%,
            #155e75 35%,
            #0f766e 65%,
            #be185d 120%
        );

    border: 1px solid rgba(103,232,249,0.25);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.40),
        inset 0 1px 0 rgba(255,255,255,0.12);
}

.hero::before {
    content: "";
    position: absolute;

    width: 420px;
    height: 420px;

    right: -150px;
    top: -180px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(103,232,249,0.25),
            transparent 65%
        );
}

.hero::after {
    content: "";

    position: absolute;

    width: 250px;
    height: 250px;

    left: 40%;
    bottom: -180px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(244,114,182,0.20),
            transparent 65%
        );
}

.hero-title {
    position: relative;
    z-index: 2;

    font-size: 44px;
    font-weight: 800;

    color: white;

    letter-spacing: -1.5px;
}

.hero-subtitle {
    position: relative;
    z-index: 2;

    margin-top: 12px;

    font-size: 17px;

    color: #cffafe;

    max-width: 750px;
}


.metric-card {
    padding: 25px;
    min-height: 145px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(15,118,110,0.28),
            rgba(15,23,42,0.70)
        );

    border: 1px solid rgba(45,212,191,0.18);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.25);

    backdrop-filter: blur(15px);

    transition: 0.25s;
}

.metric-card:hover {
    transform: translateY(-4px);

    border-color: rgba(103,232,249,0.45);

    box-shadow:
        0 20px 50px rgba(6,182,212,0.15);
}

.metric-icon {
    font-size: 27px;
}

.metric-title {
    margin-top: 7px;
    color: #94a3b8;
    font-size: 13px;
}

.metric-value {
    margin-top: 6px;

    font-size: 31px;
    font-weight: 800;

    color: #f0fdfa;
}


.section-title {
    margin-top: 40px;
    margin-bottom: 20px;

    font-size: 26px;
    font-weight: 800;

    color: #ecfeff;
}


button[data-baseweb="tab"] {
    color: #94a3b8 !important;
    font-weight: 700;
    font-size: 15px;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #67e8f9 !important;
}


.prediction-box {
    padding: 30px;
    margin-top: 10px;

    border-radius: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(8,51,68,0.90),
            rgba(15,23,42,0.90),
            rgba(76,5,25,0.55)
        );

    border: 1px solid rgba(103,232,249,0.20);

    box-shadow:
        0 20px 55px rgba(0,0,0,0.30);
}

.prediction-title {
    color: white;
    font-size: 22px;
    font-weight: 800;
}

.prediction-text {
    color: #94a3b8;
    font-size: 15px;
    margin-top: 8px;
}


div[data-testid="stExpander"] {
    background: linear-gradient(135deg, rgba(15,23,42,0.75), rgba(8,51,68,0.45)) !important;
    border: 1px solid rgba(103,232,249,0.25) !important;
    border-radius: 14px !important;
    margin-top: 14px !important;
    overflow: hidden !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}

div[data-testid="stExpander"]:hover {
    border-color: rgba(103,232,249,0.5) !important;
    box-shadow: 0 6px 20px rgba(6, 182, 212, 0.15) !important;
    transform: translateY(-2px);
}

div[data-testid="stExpander"] summary {
    padding: 14px 18px !important;
}

div[data-testid="stExpander"] summary p {
    color: #ecfeff !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
}

div[data-testid="stExpander"] summary svg {
    fill: #67e8f9 !important;
    width: 20px !important;
    height: 20px !important;
}


.stButton > button {
    width: 100%;

    border: none;
    border-radius: 14px;

    padding: 13px;

    color: white;

    font-size: 16px;
    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #0891b2,
            #14b8a6,
            #ec4899
        );

    box-shadow:
        0 10px 30px rgba(20,184,166,0.25);

    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 15px 35px rgba(236,72,153,0.25);
}


.footer {
    text-align: center;

    margin-top: 55px;
    padding: 25px;

    color: #64748b;

    border-top:
        1px solid rgba(255,255,255,0.06);
}

</style>
""", unsafe_allow_html=True)


# ===========================
# LOAD DATA + MODEL
# ===========================

@st.cache_resource
def load_model():
    return joblib.load("hotel_cancellation_model.pkl")


@st.cache_data
def load_data():
    return pd.read_csv("hotel_cancellation_data.csv")


model = load_model()
df = load_data()


# ===========================
# HANDLE MISSING VALUES
# ===========================

categorical_columns = [
    "hotel",
    "arrival_date_month",
    "meal",
    "country",
    "market_segment",
    "distribution_channel",
    "reserved_room_type",
    "assigned_room_type",
    "deposit_type",
    "customer_type"
]

numerical_columns = [
    "lead_time",
    "arrival_date_year",
    "arrival_date_week_number",
    "arrival_date_day_of_month",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "babies",
    "is_repeated_guest",
    "previous_cancellations",
    "previous_bookings_not_canceled",
    "booking_changes",
    "agent",
    "days_in_waiting_list",
    "adr",
    "required_car_parking_spaces",
    "total_of_special_requests"
]

for col in categorical_columns:
    if col in df.columns:
        df[col] = df[col].fillna(
            df[col].mode()[0]
            if not df[col].mode().empty
            else "Unknown"
        )

for col in numerical_columns:
    if col in df.columns:
        df[col] = df[col].fillna(
            df[col].median()
        )


# ===========================
# HERO
# ===========================

st.markdown("""
<div class="hero">
    <div class="hero-title">🏨 Hotel Cancellation AI</div>
    <div class="hero-subtitle">
        Discover booking behavior, explore cancellation patterns,
        and predict cancellation risk using Machine Learning.
    </div>
</div>
""", unsafe_allow_html=True)


# ===========================
# SIDEBAR FILTERS
# ===========================

st.sidebar.markdown(" 🎛️ Explore Data")

hotel_filter = st.sidebar.multiselect(
    "🏨 Hotel Type",
    sorted(df["hotel"].unique()),
    default=sorted(df["hotel"].unique())
)

year_filter = st.sidebar.multiselect(
    "📅 Arrival Year",
    sorted(df["arrival_date_year"].unique()),
    default=sorted(df["arrival_date_year"].unique())
)

market_filter = st.sidebar.multiselect(
    "🎯 Market Segment",
    sorted(df["market_segment"].unique()),
    default=sorted(df["market_segment"].unique())
)


filtered_df = df[
    df["hotel"].isin(hotel_filter)
    &
    df["arrival_date_year"].isin(year_filter)
    &
    df["market_segment"].isin(market_filter)
]


# ===========================
# KPI
# ===========================

total = len(filtered_df)

cancelled = filtered_df["is_canceled"].sum()

rate = (
    cancelled / total * 100
    if total > 0
    else 0
)

avg_adr = (
    filtered_df["adr"].mean()
    if total > 0
    else 0
)


c1, c2, c3, c4 = st.columns(4)


with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">📋</div>
        <div class="metric-title">Total Bookings</div>
        <div class="metric-value">{total:,}</div>
    </div>
    """, unsafe_allow_html=True)


with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">❌</div>
        <div class="metric-title">Cancelled</div>
        <div class="metric-value">{cancelled:,}</div>
    </div>
    """, unsafe_allow_html=True)


with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">📈</div>
        <div class="metric-title">Cancellation Rate</div>
        <div class="metric-value">{rate:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)


with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">💰</div>
        <div class="metric-title">Average ADR</div>
        <div class="metric-value">${avg_adr:.1f}</div>
    </div>
    """, unsafe_allow_html=True)


# ===========================
# ANALYTICS
# ===========================

st.markdown(
    '<div class="section-title">📊 Booking Analytics</div>',
    unsafe_allow_html=True
)


tab1, tab2, tab3, tab4 = st.tabs([
    "📅 Time Analysis",
    "🏨 Hotel Analysis",
    "🎯 Customer Segments",
    "💰 Revenue Analysis"
])


# ===========================
# TAB 1 — TIME
# ===========================

with tab1:

    col1, col2 = st.columns(2)

    yearly = (
        filtered_df
        .groupby("arrival_date_year")["is_canceled"]
        .mean()
        .reset_index()
    )

    yearly["is_canceled"] *= 100

    fig1 = px.line(
        yearly,
        x="arrival_date_year",
        y="is_canceled",
        markers=True,
        title="Cancellation Rate by Year",
        labels={
            "arrival_date_year": "Year",
            "is_canceled": "Cancellation Rate (%)"
        }
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    col1.plotly_chart(
        fig1,
        use_container_width=True
    )


    monthly = (
        filtered_df
        .groupby("arrival_date_month")["is_canceled"]
        .mean()
        .reset_index()
    )

    monthly["is_canceled"] *= 100

    month_order = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    monthly["arrival_date_month"] = pd.Categorical(
        monthly["arrival_date_month"],
        categories=month_order,
        ordered=True
    )

    monthly = monthly.sort_values(
        "arrival_date_month"
    )

    fig2 = px.area(
        monthly,
        x="arrival_date_month",
        y="is_canceled",
        markers=True,
        title="Monthly Cancellation Pattern",
        labels={
            "arrival_date_month": "Month",
            "is_canceled": "Cancellation Rate (%)"
        }
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    col2.plotly_chart(
        fig2,
        use_container_width=True
    )


# ===========================
# TAB 2 — HOTEL
# ===========================

with tab2:

    col1, col2 = st.columns(2)

    hotel_rate = (
        filtered_df
        .groupby("hotel")["is_canceled"]
        .mean()
        .reset_index()
    )

    hotel_rate["is_canceled"] *= 100

    fig1 = px.bar(
        hotel_rate,
        x="hotel",
        y="is_canceled",
        text_auto=".1f",
        title="Cancellation Rate by Hotel",
        labels={
            "hotel": "Hotel",
            "is_canceled": "Cancellation Rate (%)"
        }
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    col1.plotly_chart(
        fig1,
        use_container_width=True
    )


    hotel_bookings = (
        filtered_df["hotel"]
        .value_counts()
        .reset_index()
    )

    hotel_bookings.columns = [
        "hotel",
        "count"
    ]

    fig2 = px.pie(
        hotel_bookings,
        names="hotel",
        values="count",
        hole=0.55,
        title="Booking Distribution"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    col2.plotly_chart(
        fig2,
        use_container_width=True
    )


# ===========================
# TAB 3 — CUSTOMER SEGMENTS
# ===========================

with tab3:

    col1, col2 = st.columns(2)

    market_rate = (
        filtered_df
        .groupby("market_segment")["is_canceled"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    market_rate["is_canceled"] *= 100

    fig1 = px.bar(
        market_rate,
        x="is_canceled",
        y="market_segment",
        orientation="h",
        text_auto=".1f",
        title="Cancellation Rate by Market Segment",
        labels={
            "market_segment": "Market Segment",
            "is_canceled": "Cancellation Rate (%)"
        }
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    col1.plotly_chart(
        fig1,
        use_container_width=True
    )


    customer_data = (
        filtered_df["customer_type"]
        .value_counts()
        .reset_index()
    )

    customer_data.columns = [
        "customer_type",
        "count"
    ]

    fig2 = px.pie(
        customer_data,
        names="customer_type",
        values="count",
        hole=0.5,
        title="Customer Type Distribution"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    col2.plotly_chart(
        fig2,
        use_container_width=True
    )


# ===========================
# TAB 4 — REVENUE
# ===========================

with tab4:

    col1, col2 = st.columns(2)

    fig1 = px.histogram(
        filtered_df,
        x="adr",
        nbins=40,
        title="ADR Distribution",
        labels={
            "adr": "Average Daily Rate"
        }
    )

    fig1.update_traces(
        marker_color="#93c5fd"
    )

    fig1.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        bargap=0.05
    )

    col1.plotly_chart(
        fig1,
        use_container_width=True
    )

    stay_data = filtered_df.copy()
    stay_data["total_stay"] = (
        stay_data["stays_in_weekend_nights"]
        + stay_data["stays_in_week_nights"]
    )

    stay_summary = (
        stay_data
        .groupby(["market_segment", "reserved_room_type"])
        .agg(
            average_length_of_stay=("total_stay", "mean"),
            average_adr=("adr", "mean"),
            cancellation_rate=("is_canceled", lambda x: x.mean() * 100),
            bookings=("hotel", "count")
        )
        .reset_index()
    )

    fig2 = px.scatter(
        stay_summary,
        x="average_length_of_stay",
        y="average_adr",
        size="bookings",
        color="cancellation_rate",
        hover_data=["market_segment", "reserved_room_type"],
        title="ADR vs Length of Stay",
        labels={
            "average_length_of_stay": "Average Length of Stay",
            "average_adr": "Average ADR",
            "cancellation_rate": "Cancellation Rate (%)",
            "bookings": "Total Bookings"
        },
        color_continuous_scale="RdPu"
    )

    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    col2.plotly_chart(
        fig2,
        use_container_width=True
    )


# ===========================
# PREDICTION
# ===========================

st.markdown(
    '<div class="section-title">🤖 AI Cancellation Prediction</div>',
    unsafe_allow_html=True
)


# ===========================
# Prediction Description
# ===========================

st.markdown("""
<div class="prediction-box">
    <div class="prediction-title">🔮 Predict Booking Risk</div>
    <div class="prediction-text">
        Enter the booking details and let the XGBoost model
        estimate the probability of cancellation.
    </div>
</div>
""", unsafe_allow_html=True)


st.write("")


# ===========================
# INPUT SECTION 1 — BASIC BOOKING INFORMATION
# ===========================

with st.expander("📋 Basic Booking Information", expanded=True):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        hotel = st.selectbox(
            "Hotel",
            sorted(df["hotel"].unique())
        )

        arrival_year = st.selectbox(
            "Arrival Year",
            sorted(df["arrival_date_year"].unique())
        )

    with c2:

        arrival_month = st.selectbox(
            "Arrival Month",
            [
                "January", "February", "March",
                "April", "May", "June",
                "July", "August", "September",
                "October", "November", "December"
            ]
        )

        market_segment = st.selectbox(
            "Market Segment",
            sorted(df["market_segment"].unique())
        )

    with c3:

        lead_time = st.number_input(
            "Lead Time",
            min_value=0,
            max_value=1000,
            value=100
        )

        adults = st.number_input(
            "Adults",
            min_value=1,
            max_value=10,
            value=2
        )

    with c4:

        children = st.number_input(
            "Children",
            min_value=0,
            max_value=10,
            value=0
        )

        babies = st.number_input(
            "Babies",
            min_value=0,
            max_value=5,
            value=0
        )


# ===========================
# INPUT SECTION 2 — STAY & ROOM DETAILS
# ===========================

with st.expander("🛏️ Stay & Room Details", expanded=False):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        weekend_nights = st.number_input(
            "Weekend Nights",
            min_value=0,
            max_value=20,
            value=1
        )

    with c2:

        week_nights = st.number_input(
            "Week Nights",
            min_value=0,
            max_value=50,
            value=3
        )

    with c3:

        reserved_room_type = st.selectbox(
            "Reserved Room Type",
            sorted(df["reserved_room_type"].unique())
        )

    with c4:

        assigned_room_type = st.selectbox(
            "Assigned Room Type",
            sorted(df["assigned_room_type"].unique())
        )


# ===========================
# INPUT SECTION 3 — CUSTOMER & CHANNEL DETAILS
# ===========================

with st.expander("👤 Customer & Channel Details", expanded=False):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        meal = st.selectbox(
            "Meal",
            sorted(df["meal"].unique())
        )

    with c2:

        distribution_channel = st.selectbox(
            "Distribution Channel",
            sorted(df["distribution_channel"].unique())
        )

    with c3:

        customer_type = st.selectbox(
            "Customer Type",
            sorted(df["customer_type"].unique())
        )

    with c4:

        deposit_type = st.selectbox(
            "Deposit Type",
            sorted(df["deposit_type"].unique())
        )


# ===========================
# INPUT SECTION 4 — BOOKING & REVENUE DETAILS
# ===========================

with st.expander("💰 Booking & Revenue Details", expanded=False):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        adr = st.number_input(
            "ADR",
            min_value=0.0,
            max_value=1000.0,
            value=100.0
        )

    with c2:

        booking_changes = st.number_input(
            "Booking Changes",
            min_value=0,
            max_value=100,
            value=0
        )

    with c3:

        total_special_requests = st.number_input(
            "Special Requests",
            min_value=0,
            max_value=10,
            value=0
        )

    with c4:

        required_parking = st.number_input(
            "Required Parking Spaces",
            min_value=0,
            max_value=10,
            value=0
        )


# ===========================
# PREDICT BUTTON
# ===========================

st.write("")

if st.button("🚀 Predict Cancellation"):

    input_data = pd.DataFrame({
        "hotel": [hotel],
        "lead_time": [lead_time],
        "arrival_date_year": [arrival_year],
        "arrival_date_month": [arrival_month],
        "arrival_date_week_number": [26], 
        "arrival_date_day_of_month": [15], 
        "stays_in_weekend_nights": [weekend_nights],
        "stays_in_week_nights": [week_nights],
        "adults": [adults],
        "children": [children],
        "babies": [babies],
        "meal": [meal],
        "country": ["PRT"], 
        "market_segment": [market_segment],
        "distribution_channel": [distribution_channel],
        "is_repeated_guest": [0], 
        "previous_cancellations": [0],
        "previous_bookings_not_canceled": [0],
        "reserved_room_type": [reserved_room_type],
        "assigned_room_type": [assigned_room_type],
        "booking_changes": [booking_changes],
        "deposit_type": [deposit_type],
        "agent": [0], 
        "days_in_waiting_list": [0],
        "customer_type": [customer_type],
        "adr": [adr],
        "required_car_parking_spaces": [required_parking],
        "total_of_special_requests": [total_special_requests]
    })

    try:
        probability = model.predict_proba(input_data)[0][1]
        prediction = model.predict(input_data)[0]
        probability_percent = probability * 100

        if prediction == 1:
            st.error(f"⚠️ High Cancellation Risk — {probability_percent:.1f}%")
        else:
            st.success(f"✅ Low Cancellation Risk — {probability_percent:.1f}%")

        st.progress(float(probability))

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Cancellation Probability", f"{probability_percent:.1f}%")

        with c2:
            st.metric(
                "Prediction",
                "Cancelled" if prediction == 1 else "Not Cancelled"
            )

    except Exception as e:
        st.error("Prediction failed. Please check that the input features match the model.")
        st.code(str(e))

# ===========================
# FOOTER
# ===========================

st.markdown("""
<div class="footer">
    🏨 <b>Hotel Cancellation AI</b><br><br>
    Machine Learning • Data Analytics • Interactive Visualization
</div>
""", unsafe_allow_html=True)
