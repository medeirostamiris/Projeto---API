from flask import Blueprint, jsonify, request
from controllers.item_controller import get_items_controller, criar_item_controller

item_routes = Blueprint("item_routes", __name__)

@item_routes.route("/items", methods=["GET"])
def get_items():
    return jsonify(get_items_controller()), 200


@item_routes.route("/items", methods=["POST"])
def criar_item_route():
    dados = request.get_json()
    resposta, status = criar_item_controller(dados)
    return jsonify(resposta), status
