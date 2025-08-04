from flask import Flask, jsonify, request, send_from_directory
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(mongo_uri)
db = client["testdb"]
collection = db["items"]

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    collection.insert_one(data)
    return jsonify({"msg": "Item added"}), 201

@app.route("/items", methods=["GET"])
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
