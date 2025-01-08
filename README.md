# Bank Customer Churn Prediction Using XGBoost
This repository contains a machine learning project aimed at predicting and analyzing customer churn in the banking sector using the **XGBoost** algorithm. The focus is on generating insights that enhance customer retention strategies and improve business profitability.

---

## 📖 Overview
This project identifies customers at risk of leaving a bank and provides actionable insights to retain them. By leveraging machine learning with XGBoost, the system achieves high prediction accuracy, helping financial institutions minimize losses and improve customer loyalty.

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)

---

## Introduction

Customer churn is a major issue in the banking sector, where customers have multiple options for managing their finances. This project uses the XGBoost algorithm to predict customers likely to churn, enabling targeted retention strategies.

---

## ✨ Features

- **Predictive Modeling**: Uses XGBoost for churn prediction with hyperparameter tuning.
- **Exploratory Data Analysis**: Visualizes customer demographics, transaction patterns, and churn distribution.
- **Feature Importance**: Identifies critical factors driving customer churn.
- **Real-World Application**: Enables banks to implement proactive retention strategies.

---

## 📂 Project Structure

```plaintext
bank-customer-churn-prediction/
├── README.md                 # Project documentation
├── LICENSE                   # License for the project
├── requirements.txt          # Python dependencies
├── data/                     # Dataset files
│   ├── raw_data.csv
│   ├── processed_data.csv
├── notebooks/                # Jupyter notebooks
│   ├── data_analysis.ipynb
│   ├── model_training.ipynb
│   ├── results_visualization.ipynb
├── src/                      # Source code files
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── evaluation.py
├── images/                   # Visualization images
│   ├── feature_importance.png
│   ├── results_plot.png
└── docs/                     # Documentation files
    ├── project_report.pdf
    ├── references.md
```

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3.8+
- **Libraries**:
  - [XGBoost](https://xgboost.readthedocs.io/)
  - [Pandas](https://pandas.pydata.org/)
  - [NumPy](https://numpy.org/)
  - [Matplotlib](https://matplotlib.org/)
  - [Seaborn](https://seaborn.pydata.org/)
- **Development Environment**: Jupyter Notebook

---

## 📥 Installation

### Prerequisites

- Python 3.8+
- Libraries: `xgboost`, `scikit-learn`, `pandas`, `matplotlib`, `seaborn`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/adithi741/bank-customer-churn-prediction.git
   ```
2. Navigate to the directory:
   ```bash
   cd bank-customer-churn-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 1. Prepare the Dataset
- Place your dataset in the `data/` folder.
- Ensure the file is named `raw_data.csv`.

### 2. Run the Notebooks
- Open and execute the notebooks under `notebooks/` in Jupyter or Colab:
  - [`data_analysis.ipynb`](notebooks/data_analysis.ipynb): Analyze and visualize data.
  - [`model_training.ipynb`](notebooks/model_training.ipynb): Train the XGBoost model.
  - [`results_visualization.ipynb`](notebooks/results_visualization.ipynb): View results and feature importance.

### 3. Execute Scripts
- Use Python scripts for automation:
  ```bash
  python src/data_preprocessing.py
  python src/model_training.py
  python src/evaluation.py
  ```

---

## 📊 Results

- **Accuracy**: Achieved 95% prediction accuracy.
- **Key Features Identified**:
  1. Account Balance
  2. Customer Age
  3. Transaction Frequency
- **Visualizations**: Feature importance and performance metrics saved in the `images/` folder.

---

## 🔮 Future Enhancements

- Integrate external datasets for enriched predictions.
- Implement SHAP for advanced model interpretability.
- Deploy the model for real-time predictions.
- Experiment with ensemble models to improve accuracy.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 📚 References

- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Kaggle: Customer Churn Dataset](https://www.kaggle.com/)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
