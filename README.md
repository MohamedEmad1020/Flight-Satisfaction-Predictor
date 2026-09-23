# ✈️ Flight Satisfaction Predictor

[![Streamlit](https://img.shields.io/badge/Streamlit-Live_App-red?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine_Learning-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?logo=plotly)](https://plotly.com/python/)

---

## 🚀 Live Demo

👉 **Try the application:**
https://flight-satisfaction-predictorflight-satisfaction-predictor-29a.streamlit.app/

👉 **GitHub Repository:**
https://github.com/MohamedEmad1020/Flight-Satisfaction-Predictor

---

## 📌 Overview

**Flight Satisfaction Predictor** is an end-to-end Machine Learning project that predicts whether an airline passenger is **Satisfied** or **Neutral/Dissatisfied** based on passenger information, travel details, and airline service ratings.

The project covers the complete Machine Learning workflow, starting from data cleaning and exploratory analysis, through preprocessing and model comparison, and ending with an interactive **Streamlit web application** for real-time predictions.

The application also provides visual analysis of the dataset and displays the model's prediction probability and feature importance.

---

## ⚙️ Features

* 🎯 Passenger satisfaction prediction
* 📊 Interactive Exploratory Data Analysis
* 🔎 Feature correlation analysis
* 📈 Interactive Plotly visualizations
* 🤖 Multiple Machine Learning models tested
* 🌲 Random Forest final prediction model
* 📋 Passenger and flight information input
* ⭐ Airline service rating analysis
* 📊 Prediction probability
* 🔍 Feature importance visualization
* ☁️ Streamlit Community Cloud deployment
* 🧩 Saved preprocessing and trained model using Joblib

---

## 🛠️ Tech Stack

| Layer                 | Tools                     |
| --------------------- | ------------------------- |
| **Programming**       | Python                    |
| **Web Application**   | Streamlit                 |
| **Machine Learning**  | Scikit-learn              |
| **Data Processing**   | Pandas, NumPy             |
| **Visualization**     | Plotly                    |
| **Model Persistence** | Joblib                    |
| **Deployment**        | Streamlit Community Cloud |

---

# 📂 Project Structure

```text
Flight-Satisfaction-Predictor/
│
├── app.py
│
├── views/
│   ├── home.py
│   ├── eda.py
│   └── predict.py
│
├── model/
│
├── catboost_info/
│
├── satisfaction_model.pkl
├── eda_data.pkl
│
├── utils.py
├── requirements.txt
└── README.md
```

### 📄 Main Files

| File                     | Description                                    |
| ------------------------ | ---------------------------------------------- |
| `app.py`                 | Main Streamlit application                     |
| `views/home.py`          | Home page and project overview                 |
| `views/eda.py`           | Exploratory Data Analysis dashboard            |
| `views/predict.py`       | Interactive prediction interface               |
| `utils.py`               | Shared application utilities and model loading |
| `satisfaction_model.pkl` | Trained model and preprocessing components     |
| `eda_data.pkl`           | Data used by the EDA dashboard                 |
| `requirements.txt`       | Required Python dependencies                   |

---

# 🧠 Machine Learning Overview

### 🎯 Problem Type

**Binary Classification**

The model predicts:

```text
Satisfied
Neutral / Dissatisfied
```

### 🎯 Target Variable

```text
satisfaction
```

### 🌲 Final Model

**Random Forest Classifier**

Random Forest was selected after comparing multiple classification algorithms during the model development process.

The model receives passenger and service information and returns:

* Predicted satisfaction class
* Prediction probability
* Feature importance

---

# 🤖 Models Explored

Several classification algorithms were experimented with during the project:

* Logistic Regression
* K-Nearest Neighbors
* Support Vector Machine
* Decision Tree
* Random Forest
* AdaBoost
* Gradient Boosting
* XGBoost
* LightGBM
* CatBoost

The final deployed application uses **Random Forest**.

---

# 🔄 Training Workflow

The Machine Learning workflow follows these steps:

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis
     │
     ▼
Feature Selection
     │
     ▼
Categorical Encoding
     │
     ▼
Feature Scaling
     │
     ▼
Model Training
     │
     ▼
Model Comparison
     │
     ▼
Random Forest Selection
     │
     ▼
Model Evaluation
     │
     ▼
Model Serialization
     │
     ▼
Streamlit Application
```

### 1. Data Cleaning

The dataset was inspected and cleaned before training.

The preprocessing stage included:

* Handling missing values
* Removing duplicate records
* Removing unnecessary columns
* Preparing categorical and numerical features

### 2. Exploratory Data Analysis

The dataset was analyzed to understand:

* Passenger satisfaction distribution
* Relationships between features
* Service-rating patterns
* Differences between satisfied and dissatisfied passengers

### 3. Feature Selection

Correlation and exploratory analysis were used to identify useful features and remove weak or unnecessary variables.

### 4. Encoding

Categorical features were transformed into numerical values so they could be used by the Machine Learning models.

### 5. Scaling

Numerical features were standardized using:

```python
StandardScaler
```

### 6. Model Training

Multiple classification algorithms were trained and evaluated.

### 7. Final Model

Random Forest was selected as the model used in the deployed application.

### 8. Model Persistence

The trained model and required preprocessing components were serialized using:

```python
joblib
```

and stored in:

```text
satisfaction_model.pkl
```

---

# 📊 Dataset

The project uses an **Airline Passenger Satisfaction** dataset containing passenger information, flight details, and service ratings.

The dataset includes information related to:

### 👤 Passenger Information

* Gender
* Age
* Customer Type

### ✈️ Flight Information

* Type of Travel
* Class
* Flight Distance
* Departure Delay
* Arrival Delay

### ⭐ Service Ratings

* Inflight Wi-Fi Service
* Ease of Online Booking
* Food and Drink
* Online Boarding
* Seat Comfort
* Inflight Entertainment
* On-board Service
* Leg Room Service
* Baggage Handling
* Check-in Service
* Inflight Service
* Cleanliness

### 🎯 Target

```text
satisfaction
```

The target contains two classes:

```text
satisfied
neutral or dissatisfied
```

---

# 🔍 Features Used by the Prediction Model

The deployed prediction system uses passenger, flight, and service-related information.

### 👤 Passenger

* Gender
* Customer Type

### ✈️ Travel

* Type of Travel
* Class
* Flight Distance

### ⭐ Service Ratings

* Inflight Wi-Fi Service
* Food and Drink
* Online Boarding
* Seat Comfort
* Inflight Entertainment
* On-board Service
* Leg Room Service
* Baggage Handling
* Check-in Service
* Inflight Service
* Cleanliness

---

# 🖥️ Application Pages

## 🏠 Home

The Home page provides an overview of the project and its Machine Learning workflow.

It includes:

* Project description
* Dataset overview
* Model information
* Model performance
* Machine Learning workflow
* Important project insights

---

## 📊 EDA — Exploratory Data Analysis

The EDA page provides an interactive exploration of the dataset using Plotly.

The analysis covers:

### 1. Satisfaction Distribution

Shows the distribution of satisfied and neutral/dissatisfied passengers.

### 2. Feature Relationships

Explores relationships between passenger satisfaction and different numerical features.

### 3. Service Ratings

Compares service ratings between satisfied and dissatisfied passengers.

### 4. Passenger Characteristics

Analyzes satisfaction according to passenger characteristics such as:

* Gender
* Customer Type
* Type of Travel
* Class

### 5. Correlation Analysis

A correlation heatmap is used to understand relationships between numerical features.

---

# 🔮 Prediction

The Prediction page allows users to enter information about a passenger and receive a satisfaction prediction.

### Passenger Information

Users can enter:

* Gender
* Customer Type
* Type of Travel
* Class
* Flight Distance

### Service Ratings

Users can rate:

* 📶 Inflight Wi-Fi
* 🍽️ Food & Drink
* 🎫 Online Boarding
* 💺 Seat Comfort
* 🎬 Inflight Entertainment
* 🧑‍✈️ On-board Service
* 🦵 Leg Room
* 🧳 Baggage Handling
* 📝 Check-in Service
* ✈️ Inflight Service
* 🧼 Cleanliness

---

# 📈 Prediction Output

After submitting the passenger information, the application provides:

### 🎯 Prediction

```text
Satisfied
```

or

```text
Neutral / Dissatisfied
```

### 📊 Prediction Probability

The application displays the probability associated with the prediction.

### 🔥 Feature Importance

The application also displays the importance of the features used by the Random Forest model.

This provides additional insight into which features were most influential for the trained model.

---

# 🔎 Key Insights

The exploratory analysis highlighted several important relationships between airline service quality and passenger satisfaction.

### ⭐ Service Quality

Service-related variables show strong relationships with overall passenger satisfaction.

Features such as:

* Online Boarding
* Inflight Entertainment
* Seat Comfort
* Inflight Wi-Fi
* On-board Service
* Leg Room

are particularly useful for understanding differences between satisfied and dissatisfied passengers.

### 👥 Passenger Characteristics

Satisfaction patterns also differ across passenger groups and travel characteristics.

### ✈️ Flight Experience

The overall passenger experience is influenced by multiple factors rather than a single service.

---

# 📊 Model Evaluation

The models were evaluated using classification metrics during the development process.

The evaluation included metrics such as:

* Accuracy
* F1 Score
* Classification performance

The final Random Forest model was selected for the deployed application based on the model comparison performed during development.

> Model performance can vary depending on the train/test split, preprocessing pipeline, and evaluation setup.

---

# ⚙️ Requirements

The project dependencies are listed in:

```text
requirements.txt
```

Main libraries include:

```text
streamlit
pandas
numpy
scikit-learn
plotly
joblib
```

---

# 💻 How to Run Locally

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/MohamedEmad1020/Flight-Satisfaction-Predictor.git
```

```bash
cd Flight-Satisfaction-Predictor
```

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

### 🌐 Live Application

https://flight-satisfaction-predictorflight-satisfaction-predictor-29a.streamlit.app/

### 📂 GitHub Repository

https://github.com/MohamedEmad1020/Flight-Satisfaction-Predictor

The Streamlit application uses:

```text
app.py
```

as its main entry point.

---

# 🔮 Future Improvements

Possible future improvements include:

* Hyperparameter tuning with GridSearchCV / RandomizedSearchCV
* Cross-validation
* SHAP model explainability
* Better model interpretability
* Automated model retraining
* Model monitoring
* FastAPI backend
* Docker deployment
* MLflow experiment tracking
* Batch prediction
* Model versioning
* More advanced feature engineering

---

# ⚠️ Limitations

This project is primarily intended as a Machine Learning portfolio project.

The predictions represent estimates based on patterns learned from the dataset.

The model does not establish causal relationships between individual services and passenger satisfaction.

Performance may also vary when the model is applied to data from different airlines, populations, or time periods.

---

# 👨‍💻 Author

## Mohamed Emad

GitHub:
https://github.com/MohamedEmad1020

Project Repository:
https://github.com/MohamedEmad1020/Flight-Satisfaction-Predictor

---

## ⭐ Project

If you find this project interesting, feel free to explore the repository and try the live application.

**Built with Python, Scikit-learn, Plotly, and Streamlit.**
