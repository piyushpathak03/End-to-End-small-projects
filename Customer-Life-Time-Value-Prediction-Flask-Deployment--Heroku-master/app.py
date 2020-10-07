import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
regressor = pickle.load(open('RF_KModel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        Income = request.form["Income"]
        Monthly_Premium_Auto = float(request.form["Monthly_Premium_Auto"])
        Months_Since_Last_Claim = float(request.form["Months_Since_Last_Claim"])
        Months_Since_Policy_Inception = float(request.form["Months_Since_Policy_Inception"])
        Number_of_Policies = float(request.form["Number_of_Policies"])
        Total_Claim_Amount = float(request.form["Total_Claim_Amount"])        
        distance = float(request.form["distance"])
        
        
        prediction=regressor.predict([[
            Income,
            Monthly_Premium_Auto,
            Months_Since_Last_Claim,
            Months_Since_Policy_Inception,
            Number_of_Policies,
            Total_Claim_Amount,
            distance
        ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Customer Life Time price is Rs. {}".format(output))


    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug=True)