# 🩺 Diabetes Prediction using Machine Learning

A machine learning project that predicts whether a person is **diabetic or non-diabetic** using the **PIMA Diabetes Dataset** and a **Support Vector Machine (SVM)** classifier.

---

## 📌 Project Overview

This project uses supervised machine learning to classify patients based on diagnostic measurements. Given medical input data, the model predicts the likelihood of diabetes.

- **Dataset:** PIMA Indians Diabetes Dataset (`diabetes.csv`)
- **Algorithm:** Support Vector Machine (SVM) with Linear Kernel
- **Task:** Binary Classification (`0` = Non-Diabetic, `1` = Diabetic)

---

## 📂 Project Structure

```
├── DIABETES_PREDICTION.ipynb   # Main Jupyter Notebook
├── diabetes.csv                # Dataset file
└── README.md                   # Project documentation
```

---

## 📊 Dataset Description

The dataset contains medical records for **female patients** with the following features:

| Feature                    | Description                              |
|---------------------------|------------------------------------------|
| `Pregnancies`              | Number of pregnancies                    |
| `Glucose`                  | Plasma glucose concentration             |
| `BloodPressure`            | Diastolic blood pressure (mm Hg)         |
| `SkinThickness`            | Triceps skinfold thickness (mm)          |
| `Insulin`                  | 2-Hour serum insulin (mu U/ml)           |
| `BMI`                      | Body mass index (weight in kg/(height in m)²) |
| `DiabetesPedigreeFunction` | Diabetes pedigree function               |
| `Age`                      | Age in years                             |
| `Outcome`                  | Target variable (0 = Non-Diabetic, 1 = Diabetic) |

---

## 🔧 Tech Stack & Dependencies

```
Python 3.x
numpy
pandas
scikit-learn
```

Install all dependencies:

```bash
pip install numpy pandas scikit-learn
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/diabetes-prediction.git
   cd diabetes-prediction
   ```

2. **Make sure `diabetes.csv` is in the same directory as the notebook**

3. **Open the Jupyter Notebook**
   ```bash
   jupyter notebook DIABETES_PREDICTION.ipynb
   ```

4. **Run all cells** from top to bottom

---

## 🧠 ML Pipeline

```
1. Data Loading          →  Load diabetes.csv using pandas
2. Data Analysis         →  Explore shape, statistics, outcome distribution
3. Feature/Label Split   →  X = features, Y = Outcome
4. Data Standardization  →  StandardScaler (zero mean, unit variance)
5. Train-Test Split      →  80% train, 20% test (stratified, random_state=2)
6. Model Training        →  SVM with linear kernel
7. Model Evaluation      →  Accuracy on train & test sets
8. Prediction            →  Predict diabetes for new patient input
```

---

## 📈 Model Performance

| Dataset       | Accuracy  |
|---------------|-----------|
| Training Data | ~78–80%   |
| Test Data     | ~77–79%   |

> *Note: Actual accuracy may vary slightly based on the dataset version.*

---

## 🔮 Making a Prediction

To predict for a new patient, update the `input_data` dictionary in the notebook:

```python
input_data = {
    'Pregnancies': [2],
    'Glucose': [138],
    'BloodPressure': [62],
    'SkinThickness': [35],
    'Insulin': [0],
    'BMI': [33.6],
    'DiabetesPedigreeFunction': [0.351],
    'Age': [21]
}
```

**Output:**
```
The person is not diabetic
```
or
```
The person is diabetic
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👤 Author

Made with ❤️ for learning and practice in Machine Learning.
