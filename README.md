# Price Prediction

## Overview
This project aims to predict the price of rooms using various machine learning techniques. The model was developed with a thorough process including data cleaning, exploratory data analysis (EDA), outlier detection and removal, and deployment using Flask.

## Project Description
The objective of this project is to predict hotel room prices based on various features. The process involves:

- Cleaning the dataset to handle missing values and inconsistencies.
- Performing EDA to understand the data better and uncover patterns.
- Detecting and removing outliers to improve model performance.
- Training a machine learning model to predict prices.
- Deploying the model using Flask for easy accessibility.

## Installation
To run this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/KRISHNA-JAIN15/Airbnb-price-prediction.git
    cd Airbnb-price-prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the prediction interface.

## Dataset
The dataset used for this project contains various features related to hotel bookings. Ensure you have the dataset in the `data` directory before running the scripts.

## Data Cleaning
Data cleaning steps include:
- Handling missing values.
- Converting data types.
- Removing duplicate entries.

## Exploratory Data Analysis (EDA)
EDA was performed to:
- Understand the distribution of features.
- Visualize relationships between variables.
- Identify trends and patterns.

## Outlier Detection and Removal
Outliers were detected using statistical methods and visualizations. These outliers were removed to enhance model accuracy.

## Model Training
Various machine learning algorithms were tested, and the best-performing model was selected. The training process involved:
- Splitting the data into training and testing sets.
- Hyperparameter tuning.
- Evaluating model performance using metrics like RMSE, MAE, and R^2 score.

## Deployment
The trained model was deployed using Flask. The application allows users to input features and get predicted room prices.

## Contributing
Contributions are welcome! Please create a pull request with detailed information on your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
