from flask import Flask, render_template, request, jsonify
from api import app, database, bcrypt
from api.models import Membro, Usuario
# from api.authentication import jwt_required
import datetime
import json

@app.route('/membros', methods=["POST"])
def novo_membro():
    membro_novo = request.get_json()
    membro_novo = json.loads(membro_novo)
    membro = Membro(nome=membro_novo['nome'],
                    data_nascimento=membro_novo['data_nascimento'],
                    numero=membro_novo['numero'],
                    endereco=membro_novo['endereco'],
                    cargo=membro_novo['cargo'])
    database.session.add(membro)
    database.session.commit()
    membro_json = Membro.query.filter_by(nome=membro_novo['nome']).first().__dict__
    treat = membro_json.pop('_sa_instance_state')
    return jsonify(membro_json)

@app.route('/membros', methods=["GET"])
def mostrar_membros():
    lista_membros = []
    membros = Membro.query.all()
    for l in membros:
        l = l.__dict__
        treat = l.pop('_sa_instance_state')
        lista_membros.append(l)
    return jsonify(lista_membros)

@app.route('/membros', methods=["DELETE"])
def deletar_membro():
    membro_json = request.get_json()
    membro_obj = Membro.query.filter_by(id=membro_json['id']).first()
    database.session.delete(membro_obj)
    database.session.commit()
    lista_membros = []
    membros = Membro.query.all()
    for l in membros:
        l = l.__dict__
        treat = l.pop('_sa_instance_state')
        lista_membros.append(l)
    return jsonify(lista_membros)

@app.route('/membros', methods=["PUT"])
def editar_membro():
    membro_json = request.get_json()
    membro_json = json.loads(membro_json)
    membro_obj = Membro.query.filter_by(id=membro_json['id']).first()   
    membro_obj.nome = membro_json['nome']
    membro_obj.data_nascimento = membro_json['data_nascimento']
    membro_obj.numero = membro_json['numero']
    membro_obj.endereco = membro_json['endereco']
    membro_obj.cargo = membro_json['cargo']
    database.session.commit()
    membro_obj = Membro.query.filter_by(id=membro_json['id']).first()
    lista_membros = []
    membros = Membro.query.all()
    for l in membros:
        l = l.__dict__
        treat = l.pop('_sa_instance_state')
        lista_membros.append(l)
    return jsonify(lista_membros)

@app.route('/usuarios', methods=["GET"])
def mostrar_usuarios():
    lista_usuarios = []
    usuarios = Usuario.query.all()
    for l in usuarios:
        l = l.__dict__
        treat = l.pop('_sa_instance_state')
        lista_usuarios.append(l)
    return jsonify(lista_usuarios)

@app.route('/login', methods=["POST"])
def auth():
    usuario_json = request.get_json()
    usuario_obj = Usuario.query.filter_by(email=usuario_json['email']).first()

    if not usuario_obj:
        return jsonify({"error": "usuario não encontrado."})

    verify = usuario_obj.verify_password(usuario_json['senha'])

    if not verify:
        return jsonify({"error": "senha incorreta."})

    return jsonify({"auth": True})

# @app.route('/protected')
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify({"usuario_atual": current_user}), 200
