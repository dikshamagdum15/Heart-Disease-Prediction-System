# ❤️ Heart Disease Prediction System

- A Machine Learning–based Heart Disease Prediction System that predicts whether a person is likely to have heart disease based on medical parameters.

- This project uses Python, MySQL, and ML algorithms to analyze patient data and provide predictions.

## 📌 Project Overview

- Heart disease is one of the leading causes of death worldwide. Early prediction can help in timely treatment and prevention.

- This system uses a trained machine learning model on a medical dataset to predict heart disease risk.

## 🛠️ Technologies Used

Python 3

MySQL Database

Pandas, NumPy

Scikit-learn

Matplotlib / Seaborn (for visualization)

## 📂 Project Structure

**Heart Disease Prediction System/**

│
├── backend.py          # Backend logic for prediction

├── main.py             # Main program execution file

├── MySQL.py            # Database connectivity and operations

├── heart.csv           # Dataset used for training/testing

├── requirements.txt    # Required Python libraries

├── OUTPUT.docx         # Sample output & results

├── Images/             # Project screenshots

└── __pycache__/        # Cache files

## 📊 Dataset
File: heart.csv

**Contains medical attributes such as:**

- Age

- Sex

- Chest pain type

- Blood pressure

- Cholesterol

- Heart rate

- ECG results

Target (0 = No Heart Disease, 1 = Heart Disease)

## ⚙️ Requirements

1️⃣ **Software Requirements**

- Python 3.8 or higher

- MySQL Server

- Code Editor (VS Code recommended)


2️⃣ **Python Libraries**

All required libraries are listed in:

requirements.txt


▶️ **How to Run the Program**

**Step 1:Clone or Download the Project**

Download and extract the ZIP file.


**Step 2:Navigate to Project Folder**

cd "Heart Disease Prediction System"


**Step 3:Install Required Libraries**

pip install -r requirements.txt


**Step 4: Setup MySQL Database**

Start MySQL Server

Create a database (example):

CREATE DATABASE heart_disease;

Update your MySQL credentials inside MySQL.py


**Step 5: Run the Application**

python main.py

# 📈 Output

- Displays prediction results in the console

- Indicates whether the patient has heart disease or not

- Sample outputs are provided in OUTPUT.docx

# ✅ Features

- User-friendly prediction flow

- Accurate ML-based results

- Database integration using MySQL

- Easy to run and modify

- Well-structured codebase

