# 🏨 Hotel Cancellation AI

An interactive **Hotel Booking Analytics & Cancellation Prediction** application built with **Python, Machine Learning, Streamlit, and Plotly**.

The project analyzes hotel booking patterns, explores cancellation behavior, and uses an **XGBoost classification model** to estimate the probability of a booking cancellation.

---

## 🚀 Live Demo

🔗 **Streamlit Dashboard:**
https://hotel-cancellation-ai-malakmoubark-m6gsaeycytclnenmoljn5u.streamlit.app

---

## 📌 Project Overview

Hotel cancellations can have a significant impact on hotel operations and revenue.

This project provides an interactive dashboard that helps explore:

* Booking volume and cancellation rates
* Cancellation patterns over time
* Differences between hotel types
* Customer and market segment behavior
* Revenue and ADR patterns
* Cancellation risk prediction using Machine Learning

---

## 📊 Dashboard Features

### 📅 Time Analysis

Explore cancellation behavior across:

* Arrival years
* Arrival months

The dashboard visualizes cancellation rates and monthly cancellation patterns.

### 🏨 Hotel Analysis

Compare different hotel types based on:

* Cancellation rate
* Booking distribution

### 🎯 Customer Segments

Analyze:

* Cancellation rate by market segment
* Customer type distribution

### 💰 Revenue Analysis

Explore:

* ADR (Average Daily Rate) distribution
* Relationship between ADR and length of stay
* Cancellation rate across booking groups

### 🤖 AI Cancellation Prediction

The dashboard includes an interactive prediction interface powered by an **XGBoost classification model**.

Users can enter booking information such as:

* Hotel type
* Arrival year and month
* Market segment
* Lead time
* Number of guests
* Length of stay
* Room type
* Meal type
* Distribution channel
* Customer type
* Deposit type
* ADR
* Booking changes
* Special requests
* Required parking spaces

The model then provides:

* Cancellation probability
* Predicted cancellation status
* Risk level

---

## 🧹 Data Processing

The project includes:

- Data cleaning and preprocessing
- Handling missing values
- Categorical and numerical feature processing
- Feature encoding
- Exploratory Data Analysis (EDA)

---

## 🤖 Machine Learning

The project uses **XGBoost** for binary classification.

### Target Variable

`is_canceled`

* `0` → Not Cancelled
* `1` → Cancelled

The trained model is saved as:

`hotel_cancellation_model.pkl`

and loaded into the Streamlit application using `joblib`.

---

## 📈 Interactive Visualization

The dashboard is built using **Plotly**, providing interactive charts that allow users to explore the data dynamically.

The dashboard also includes filters for:

* Hotel Type
* Arrival Year
* Market Segment

These filters update the displayed KPIs and visualizations.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Streamlit
* Plotly

---

## 📂 Project Structure

```text
hotel-cancellation-ai/
│
├── app.py
├── hotel_cancellation.ipynb
├── hotel_cancellation_data.csv
├── hotel_cancellation_model.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                           | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `app.py`                       | Streamlit dashboard and prediction application              |
| `hotel_cancellation.ipynb`     | Data analysis, preprocessing, and machine learning workflow |
| `hotel_cancellation_data.csv`  | Dataset used by the application                             |
| `hotel_cancellation_model.pkl` | Trained XGBoost model                                       |
| `requirements.txt`             | Required Python libraries                                   |
| `README.md`                    | Project documentation                                       |

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/malakmoubark/hotel-cancellation-ai.git
```

### 2. Navigate to the project directory

```bash
cd hotel-cancellation-ai
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🎯 Project Goal

The main goal of this project is to combine **Data Analytics, Interactive Visualization, and Machine Learning** to better understand hotel booking behavior and identify potential cancellation risks.

---

## Author

**Malak Moubark**  
Computer Science Student — Menofia University

🔗 [LinkedIn](https://www.linkedin.com/in/malak-moubark-2b3a90352)

🔗 [GitHub](https://github.com/malakmoubark)
