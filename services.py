import requests
from flask import current_app as app

def get_variables():
    url = app.config['API_BASE_URL'] + "/api/variables"
    auth = (app.config['BASIC_AUTH_USERNAME'], app.config['BASIC_AUTH_PASSWORD'])
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        print(f"data: {data}")
        return data
    else:
        print(f"Error get_variables: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None


def get_hourly_data(variable):
    url = app.config['API_BASE_URL'] + '/api/data/variable/"{variable}"/hour'
    auth = (app.config['BASIC_AUTH_USERNAME'], app.config['BASIC_AUTH_PASSWORD'])
    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error get_hourly_data: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None

def get_daily_data(variable):
    url = app.config['API_BASE_URL'] + f'/api/data/variable/"{variable}"/day'
    auth = (app.config['BASIC_AUTH_USERNAME'], app.config['BASIC_AUTH_PASSWORD'])
    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error get_daily_data: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None

def get_history_data(variable):
    if variable:
        url = app.config['API_BASE_URL'] + f'/api/data/variable/"{variable}"/history'
    else:
        url = app.config['API_BASE_URL'] + '/api/data/history'
        
    auth = (app.config['BASIC_AUTH_USERNAME'], app.config['BASIC_AUTH_PASSWORD'])
    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error get_history_data: {response.status_code}")
        print(f"Response Body: {response.text}")
        return None

