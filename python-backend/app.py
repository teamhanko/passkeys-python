from flask import Flask, request, jsonify, session
from db import users
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import jwt

load_dotenv()

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
app.secret_key = "super-secret-key"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = next((user for user in users if user['email'] == email and user['password'] == password), None)

    if user:
        session["user_id"] = user["id"]
        session["email"] = user["email"]
        user_info = {"id": user["id"], "email": user["email"]}
        return jsonify({"message": "Login successful", "user": user_info}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/logout')
def logout_user():
    session.pop('user_id', None)
    # session.clear()
    return jsonify({"message": "You have been logged out"}), 200


#### passkeys
tenant_id = os.getenv("PASSKEY_TENANT_ID")
api_key = os.getenv("PASSKEY_API_KEY")

baseUrl = f"https://passkeys.hanko.io/{tenant_id}"
headers = {
    "apikey": api_key,
    "Content-Type": "application/json", 
}

@app.route('/passkey/start-registration', methods=["POST"])
def start_registration():
    print("registering passkey")
    if 'user_id' not in session:
        return jsonify({"error": "User must be logged in to register a passkey"}), 401

    user_id = session['user_id']
    user_email = session['email']

    payload = {
        "user_id": user_id,
        "username": user_email,
    }

    response = requests.post(f"{baseUrl}/registration/initialize", headers=headers, json=payload)
    creationOptions = response.json()
    return jsonify(creationOptions)

@app.route("/passkey/finalize-registration", methods=["POST"])
def finalize_registration():
    data = request.json

    response = requests.post(f"{baseUrl}/registration/finalize", headers=headers, json=data)
    data = response.json()

    return jsonify({"message": "Passkey registered successfully"}), 200


@app.route("/passkey/start-login", methods=["POST"])
def start_login():
    response = requests.post(f"{baseUrl}/login/initialize", headers=headers)
    login_options = response.json()

    return jsonify(login_options)

@app.route("/passkey/finalize-login", methods=["POST"])
def finalize_login():
    client_data = request.json

    response = requests.post(f"{baseUrl}/login/finalize", headers=headers, json=client_data)
    data = response.json()

    token = data.get('token')
    decoded_payload = jwt.decode(token, options={"verify_signature": False})
    
    user_id = decoded_payload.get('sub') 
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        session["user_id"] = user["id"]
        session["email"] = user["email"]
        user_info = {"id": user["id"], "email": user["email"]}
        return jsonify({"message": "Login successful", "user": user_info}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401



if __name__ == '__main__':
    app.run(debug=True)

