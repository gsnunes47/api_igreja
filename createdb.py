from api import database, app
from api.models import Membro

with app.app_context():
    database.create_all()
