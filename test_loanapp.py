import pytest
from loanapp import app


#proxy to a live server: 
@pytest.fixture
def client():
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Loan App Predictions' in response.data

def test_predict_route_get(client):
    response = client.get('/predict')
    assert response.status_code == 200
    assert b'I will make the predictions' in response.data

def test_predict_route_post(client):
    test_data = {
    "ApplicantIncome":100,
    "CreditHistory":0.0,
    "Gender":"Male",
    "LoanAmount":120000,
    "Married":"Yes" }
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json == {'Loan Approval Status':'Oops, Loan Application Rejected :('}
