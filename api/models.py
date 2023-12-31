from api import database

class Membro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    data_nascimento = database.Column(database.String, nullable=False)
    numero = database.Column(database.String, nullable=False)
    endereco = database.Column(database.String, nullable=False)
    cargo = database.Column(database.String, nullable=False)
