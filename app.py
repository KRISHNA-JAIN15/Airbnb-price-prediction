from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model.sav')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    bathrooms = float(request.form['bathrooms'])
    beds = float(request.form['beds'])
    guests = float(request.form['guests'])
    bedrooms = float(request.form['bedrooms'])
    studios = float(request.form['studios'])
    rating = float(request.form['rating'])

    input_data = np.array([[bathrooms, beds, rating , bedrooms, studios, guests]])
    predicted_price = model.predict(input_data)*0.35

    return render_template('result.html', predicted_price=round(predicted_price[0]))

if __name__ == '__main__':
    app.run(debug=True)
