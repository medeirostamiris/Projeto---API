from flask import Blueprint, jsonify, request
from controllers.item_controller import get_items_controller, criar_item_controller
from controllers.item_controller import editar_item_controller, alterar_status_controller, deletar_item_controller

item_routes = Blueprint("item_routes", __name__)

@item_routes.route("/items", methods=["GET"])
def get_items():
    return jsonify(get_items_controller()), 200

#POST /items
@item_routes.route("/items", methods=["POST"])
def criar_item_route():
    dados = request.get_json()
    resposta, status = criar_item_controller(dados)
    return jsonify(resposta), status

#PUT /items/<id>
@item_routes.route("/items/<int:id>", methods=["PUT"])
def editar_item_route(id):
    dados = request.get_json()
    resposta, status = editar_item_controller(id, dados)
    return jsonify(resposta), status

# PATCH /items/<id>/status
@item_routes.route("/items/<int:id>/status", methods=["PATCH"])
def alterar_status_route(id):
    dados = request.get_json()
    resposta, status = alterar_status_controller(id, dados)
    return jsonify(resposta), status


# DELETE /items/<id>
@item_routes.route("/items/<int:id>", methods=["DELETE"])
def deletar_item_route(id):
    resposta, status = deletar_item_controller(id)
    return jsonify(resposta), status