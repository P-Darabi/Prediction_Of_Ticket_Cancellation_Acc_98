# Ticket Cancellation Prediction

This repository contains a Jupyter Notebook that demonstrates a machine-learning model for predicting ticket cancellations with an accuracy of 98%. The project leverages a combination of data preprocessing, feature engineering, and model training using various machine learning algorithms.

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [File Descriptions](#file-descriptions)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Conclusion](#conclusion)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction
This project aims to predict ticket cancellations using machine learning techniques. The high accuracy achieved indicates the potential for practical applications in optimizing ticket sales and minimizing losses due to cancellations.

## Objectives
- **Exploring and Preprocessing Data**: Analyzing and readying the data for training and testing phases.
- **Model Building**: Employing various machine learning algorithms to predict ticket cancellations.
- **Prediction and Analysis**: Forecasting ticket cancellations and analyzing the model's performance.

## Dataset
The dataset used in this project contains historical ticket booking data, including features such as booking date, cancellation date, ticket price, and other relevant details.

Variable Name | Description
--------------|-------------
Booking Date  | The date the ticket was booked
Cancellation Date | The date the ticket was cancelled
Ticket Price  | The price of the ticket
Other Features| Additional relevant details

More details about the dataset can be found [here](https://www.kaggle.com/datasets/pkdarabi/classification-of-travel-purpose).

## File Descriptions
- `Notebooks/Ticket_Cancellation_Prediction.ipynb`: Jupyter notebook containing all stages of data exploration, preprocessing, modelling, prediction, and analysis.
- `Model/XGBoost_ROC.png`: ROC curve image for the final model's performance.
- `data/ticket_data.csv`: CSV file containing the dataset used for model training and evaluation (optional, if included).

## Data Preprocessing
Data preprocessing steps include handling missing values, encoding categorical variables, and normalizing numerical features to prepare the dataset for model training.

## Feature Engineering
Feature engineering involves creating new features from existing ones to improve the model's predictive power. Examples include time-based features, interaction terms, and aggregations.

## Model Training
Multiple machine learning algorithms are explored, including:
- Logistic Regression
- Decision Trees
- Random Forest
- Gradient Boosting

Hyperparameter tuning is performed to optimize each model's performance.

## Evaluation
Model evaluation is conducted using accuracy, precision, recall, and F1-score. Cross-validation is employed to ensure the model's robustness and generalizability.

## Results
The final model achieves an accuracy of 98% on the test set, demonstrating its effectiveness in predicting ticket cancellations.

## Conclusion
This project successfully develops a high-accuracy model for predicting ticket cancellations, providing valuable insights for the transportation industry to optimize operations and reduce losses.

## Dependencies
- Python 3.6+
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Usage
To run the notebook, clone this repository and install the required dependencies. Open the notebook in Jupyter and execute the cells.

```bash
git clone https://github.com/P-Darabi/Prediction_Of_Ticket_Cancellation_Acc_98.git
cd Prediction_Of_Ticket_Cancellation_Acc_98
pip install -r requirements.txt
jupyter notebook
