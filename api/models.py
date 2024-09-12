from api import database, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Membro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    data_nascimento = database.Column(database.String, nullable=False)
    numero = database.Column(database.String, nullable=False)
    endereco = database.Column(database.String, nullable=False)
    cargo = database.Column(database.String, nullable=False)

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    def __init__(self, email, senha):
        self.email = email
        self.senha = generate_password_hash(senha)

    def verify_password(self, pwd):
        return check_password_hash(self.senha, pwd)    

    def items(self):
        return f'{"{"}"id": "{self.id}", "email": "{self.email}", "senha": "{self.senha}"{"}"}'