from models.item_model import (
    listar_items,
    criar_item,
    buscar_item,
    atualizar_item,
    atualizar_status,
    deletar_item
)

from controllers.settings import TIPOS_PERMITIDOS, STATUS_PERMITIDOS


# GET /items
def get_items_controller():
    return listar_items()


# POST /items
def criar_item_controller(dados):

    titulo = dados.get("titulo")
    tipo = dados.get("tipo")
    status = dados.get("status")
    descricao = dados.get("descricao")
    data = dados.get("data")

    # validações
    if not titulo or len(titulo) < 3:
        return {"error": "titulo deve ter no mínimo 3 caracteres"}, 400

    if tipo not in TIPOS_PERMITIDOS:
        return {"error": "tipo inválido"}, 400

    if status not in STATUS_PERMITIDOS:
        return {"error": "status inválido"}, 400

    item_id = criar_item(titulo, tipo, status, descricao, data)

    return {
        "message": "Item criado com sucesso",
        "item": {
            "id": item_id,
            "titulo": titulo,
            "tipo": tipo,
            "status": status,
            "descricao": descricao,
            "data": data
        }
    }, 201


# PUT /items/<id>
def editar_item_controller(id, dados):

    item = buscar_item(id)

    if not item:
        return {"error": "Item não encontrado"}, 404

    titulo = dados.get("titulo")
    tipo = dados.get("tipo")
    status = dados.get("status")
    descricao = dados.get("descricao")
    data = dados.get("data")

    if tipo not in TIPOS_PERMITIDOS:
        return {"error": "tipo inválido"}, 400

    if status not in STATUS_PERMITIDOS:
        return {"error": "status inválido"}, 400

    atualizar_item(id, titulo, tipo, status, descricao, data)

    return {"message": "Item atualizado com sucesso"}, 200


# PATCH /items/<id>/status
def alterar_status_controller(id, dados):

    item = buscar_item(id)

    if not item:
        return {"error": "Item não encontrado"}, 404

    status = dados.get("status")

    if status not in STATUS_PERMITIDOS:
        return {"error": "status inválido"}, 400

    atualizar_status(id, status)

    return {"message": "Status atualizado com sucesso"}, 200


# DELETE /items/<id>
def deletar_item_controller(id):

    item = buscar_item(id)

    if not item:
        return {"error": "Item não encontrado"}, 404

    deletar_item(id)

    return {"message": "Item removido com sucesso"}, 200

