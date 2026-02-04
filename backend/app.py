import sys
import os
from flask import Flask, jsonify, send_from_directory

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from flask_cors import CORS

from models.item_model import init_db
from routes.item_route import item_routes

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory("../frontend", "index.html")

@app.route("/<path:filename>")
def frontend_files(filename):
    return send_from_directory("../frontend", filename)

app.register_blueprint(item_routes)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
