from flask import Blueprint, render_template
from database import db

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def dashboard():
    total_Pacientes = db['Pacientes'].count_documents({})
    total_Medicos  = db['Medicos'].count_documents({})
    total_Seguimiento     = db['Seguimiento'].count_documents({})
    return render_template('index.html',
        total_Pacientes=total_Pacientes,
        total_Medicos=total_Medicos,
        total_Seguimiento=total_Seguimiento
    )