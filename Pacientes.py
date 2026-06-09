from flask import Blueprint, render_template, request, redirect, url_for
from database import db 

Pacientes_bp = Blueprint('pacientes', __name__)
col = db['Pacientes']

@Pacientes_bp.route("/")
def ver_pacientes():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('pacientes.html', pacientes=lista)
@Pacientes_bp.route("/nuevo")
def formulario(): 
    return render_template('formpacientes.html')

@Pacientes_bp.route("/guardar", methods=["POST"])
def guardar():
    ultimo = col.find_one({"id_paciente": {"$type": "int"}}, sort=[("id_paciente", -1)])
    nuevo_id = (ultimo["id_paciente"] + 1) if ultimo else 1

    col.insert_one({
        "id_paciente": int(nuevo_id),
        "nombre":      request.form.get("nombre"),
        "edad":        int(request.form.get("edad")),
        "sexo":        request.form.get("sexo"),
        "Tipo_de_sangre":   request.form.get("Tipo_de_sangre"),
        "telefono":    request.form.get("telefono"), # Cambiado a 'telefono' para coincidir con la plantilla
        "alergia":     request.form.get("alergia"),
    })
    return redirect(url_for('pacientes.ver_pacientes'))

@Pacientes_bp.route("/eliminar/<int:id_paciente>")
def eliminar(id_paciente):
    col.delete_one({"id_paciente": id_paciente})
    return redirect(url_for('pacientes.ver_pacientes'))

@Pacientes_bp.route("/editar/<int:id_paciente>")
def editar(id_paciente):
    paciente = col.find_one({"id_paciente": id_paciente}, {'_id': 0})
    if not paciente:
        return redirect(url_for('pacientes.ver_pacientes'))
    return render_template('formpacientes.html', paciente=paciente)

@Pacientes_bp.route("/actualizar/<int:id_paciente>", methods=["POST"])
def actualizar(id_paciente):
    col.update_one(
        {"id_paciente": id_paciente},
        {"$set": {
            "nombre":      request.form.get("nombre"),
            "edad":        int(request.form.get("edad")),
            "sexo":        request.form.get("sexo"),
            "Tipo_de_sangre":   request.form.get("Tipo_de_sangre"),
            "num_telef":    request.form.get("telefono"),
            "alergia":     request.form.get("alergia")
        }}
    )
    return redirect(url_for('pacientes.ver_pacientes'))