# California Housing Price Prediction 🏠📉

## Project Overview
This repository contains a Machine Learning project aimed at predicting real estate prices in California. Using the California Housing dataset, the goal is to build and compare different regression models to estimate the `median_house_value` based on various demographic and geographical features.

## Dataset
* **Source:** [California Housing Prices on Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
* **Description:** The data pertains to the houses found in a given California district and some summary stats about them based on the 1990 census data. It contains 20,640 entries.
* **Key Features:** * `longitude`, `latitude`: Geographical coordinates.
  * `housing_median_age`: Median age of a house within a block.
  * `total_rooms`, `total_bedrooms`: Room counts for a block.
  * `population`, `households`: Demographic data of the block.
  * `median_income`: Median income for households within a block of houses (measured in tens of thousands of US Dollars).
  * `ocean_proximity`: Categorical variable indicating distance to the ocean.
* **Target Variable:** `median_house_value`

## Machine Learning Models Used
To evaluate and compare predictive performance, the following regression algorithms were implemented:
* **Linear Regression:** Serves as the baseline model to understand direct, linear relationships between features and house prices.
* **Polynomial Regression:** Used to capture non-linear relationships and interactions between various housing features.
* **Ridge Regression (L2 Regularization):** Applied to handle potential multicollinearity among features (e.g., total rooms and bedrooms) and prevent model overfitting.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

## Project Structure
```text
├── data/                   # Folder for the housing.csv file
├── notebooks/              # Jupyter notebooks for Exploratory Data Analysis (EDA) and Modeling
├── src/                    # Python scripts for data preprocessing
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies