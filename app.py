from os import environ as env
from dotenv import find_dotenv, load_dotenv

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from db import db_connection
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def renderHome():
    return render_template("home.html")

@app.route("/api/create", methods=["POST"])
def createUser():
    try:
        request_data = json.loads(request.data)
        username = request_data["username"]
        school = request_data["school"]
        birthday = request_data["birthday"]
        db_connection.insert("Users", username, school, birthday)
        return jsonify({"success": True})
    except:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=env.get("PORT"), debug=True)
