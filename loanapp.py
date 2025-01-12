from flask import Flask, request
import pickle

app = Flask(__name__)

with open("classifier.pkl", 'rb') as f:
    model = pickle.load(f)

#Add endpoints
@app.route('/')
def home():
    return '<h1>Loan App Predictions</h1>'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "I will make the predictions"
    elif request.method == 'POST':
        loan_req = request.get_json()
        print(loan_req)

        if loan_req['Gender']=='Male':
            Gender = 0
        else:
            Gender = 1
        if loan_req['Married']=='No':
            Married = 0
        else:
            Married = 1
        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        CreditHistory = loan_req['CreditHistory']

        input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]
        pred = model.predict([input_data])

        if pred == 0:
            result = 'Oops, Loan Application Rejected :('
        else:
            result = 'Hurray!! Loan Application Approved :)'

        return {'Loan Approval Status': result}