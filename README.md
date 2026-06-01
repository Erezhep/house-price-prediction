# House Price Prediction

Machine learning project for predicting residential property prices using regression models and feature engineering techniques.

## Project Overview

This project aims to estimate house prices based on property characteristics such as area, number of bedrooms, air conditioning availability, and other housing features.

The dataset contains 545 observations and includes both numerical and categorical variables, making it suitable for evaluating different regression approaches and handling multicollinearity.

## Dataset

Source:
https://www.kaggle.com/datasets/yasserh/housing-prices-dataset

Dataset Features:

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road Access
* Air Conditioning
* Preferred Area
* Parking
* Furnishing Status
* Other housing attributes

## Models

The following machine learning models were implemented and compared:

* Linear Regression
* Polynomial Regression
* Ridge Regression

## Objectives

* Predict house prices from property features
* Compare regression algorithms
* Analyze the impact of multicollinearity
* Evaluate model performance using regression metrics

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

## Project Structure

```text
data/        # Dataset
notebooks/   # EDA and experiments
models/      # Saved models
src/         # Data processing and training scripts
```

## Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Hyperparameter tuning
* Advanced feature engineering
* Model deployment with Flask or FastAPI
