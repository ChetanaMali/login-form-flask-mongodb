from flask import Flask, request, render_template
import requests
import os
#load env file
from dotenv import load_dotenv
load_dotenv() #load the env file

BACKEND_URL = os.getenv('BACKEND_URL') # URL of the backend server

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login_page():
    login_data = dict(request.form) # get the JSON data from the request and convert it to a dictionary
    requests.post(f'{BACKEND_URL}/login', json=login_data) # send a POST request to the backend server with the login data as JSON
    return 'data posted successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, debug=True)