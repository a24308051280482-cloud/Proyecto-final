from flask import Flask
from database import db

app = Flask(__name__)

from routes.index import index_bp
from routes.Pacientes import Pacientes_bp
from routes.Medicos import Medicos_bp
from routes.Seguimiento import Seguimiento_bp

app.register_blueprint(index_bp)
app.register_blueprint(Pacientes_bp, url_prefix='/Pacientes')
app.register_blueprint(Medicos_bp, url_prefix='/Medicos')
app.register_blueprint(Seguimiento_bp, url_prefix='/Seguimiento')

if __name__ == "__main__":
    app.run(debug=True)