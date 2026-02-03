import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from flask_cors import CORS

from models.item_model import init_db
from routes.item_route import item_routes

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "API Biblioteca funcionando 🚀"})

app.register_blueprint(item_routes)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
