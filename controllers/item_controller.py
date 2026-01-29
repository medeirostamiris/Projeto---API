from models.item_model import listar_items, criar_item
from controllers.settings import TIPOS_PERMITIDOS, STATUS_PERMITIDOS

def get_items_controller():
    return listar_items()


def criar_item_controller(dados):
    titulo = dados.get("titulo")
    tipo = dados.get("tipo")
    status = dados.get("status")
    descricao = dados.get("descricao")
    data = dados.get("data")

    # validações obrigatórias
    if not titulo or len(titulo) < 3:
        return {"error": "titulo é obrigatório e deve ter no mínimo 3 caracteres"}, 400

    if tipo not in TIPOS_PERMITIDOS:
        return {"error": "tipo inválido"}, 400

    if status not in STATUS_PERMITIDOS:
        return {"error": "status inválido"}, 400

    criar_item(titulo, tipo, status, descricao, data)

    return {
        "message": "Item criado com sucesso",
        "item": {
            "titulo": titulo,
            "tipo": tipo,
            "status": status,
            "descricao": descricao,
            "data": data
        }
    }, 201
