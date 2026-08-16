# 🌫️ Air Quality & Humidity Prediction Model

A Machine Learning project that predicts **Absolute Humidity (AH)** using air-quality sensor data and environmental features.

## 🚀 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook
* Random Forest Regressor

## 📊 Dataset

The project uses the **Air Quality UCI Dataset**, containing air-quality sensor measurements and environmental features.

The target variable is:

```text
AH → Absolute Humidity
```

## ⚙️ ML Pipeline

```text
Data Ingestion
      ↓
Data Cleaning
      ↓
Feature & Target Separation
      ↓
Missing Value Handling
      ↓
Feature Scaling & Encoding
      ↓
Train-Test Split
      ↓
Random Forest Regression
      ↓
Model Evaluation
```

### Preprocessing

* Removes duplicate records
* Removes `Date` and `Time`
* Handles missing numerical values using mean imputation
* Handles categorical values using most-frequent imputation
* Applies `MinMaxScaler` to numerical features
* Applies `OneHotEncoder` to categorical features

### Model

**Random Forest Regressor**

```python
RandomForestRegressor(n_estimators=300)
```

The model is evaluated using the **R² score**.

## 📁 Project Structure

```text
Air_Quality_Humidity_Prediction_Model/
│
├── data/
│   └── AirQualityUCI.xlsx
│
├── research/
│   ├── Research Article.pdf
│   └── model.ipynb
│
├── src/
│   └── aqi/
│       ├── data_ingestion.py
│       ├── data_preprocessing.py
│       └── model_building.py
│
├── main.py
├── pyproject.toml
└── uv.lock
```

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/deveshdubey18/Air_Quality_Humidity_Prediction_Model.git
cd Air_Quality_Humidity_Prediction_Model
```

Install dependencies:

```bash
pip install -e .
```

Run:

```bash
python main.py
```

## 💾 Trained Model

The trained `model.pkl` file is available on Kaggle:

**[Download / Access the trained model on Kaggle](https://www.kaggle.com/datasets/deveshdubey18/air-quality-humidity-prediction-model)**

Use the Kaggle dataset to obtain the trained model file instead of committing the `.pkl` file directly to GitHub.

## 👨‍💻 Author

**Devesh Dubey**

[GitHub](https://github.com/deveshdubey18)
