from flask import Blueprint, render_template, request, redirect, url_for
from database import db

Seguimiento_bp = Blueprint('Seguimiento', __name__)
col = db['Seguimiento']

@Seguimiento_bp.route("/")
def ver_Seguimiento():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('Seguimiento.html', citas=lista)

@Seguimiento_bp.route("/nuevo")
def formulario():
    return render_template('formSeguimiento.html') 

@Seguimiento_bp.route("/guardar", methods=["POST"])
def guardar():
    ultimo = col.find_one({"id_cita": {"$type": "int"}}, sort=[("id_cita", -1)])
    nuevo_id = (ultimo["id_cita"] + 1) if ultimo else 1
    
    col.insert_one({
        "id_cita":    int(nuevo_id),
        "paciente":   request.form.get("paciente"),
        "id_medico":  request.form.get("id_medico"),
        "fecha":      request.form.get("fecha"),
        "costo":      request.form.get("costo"),
        "estatus":    request.form.get("estado")
    })
    return redirect(url_for('Seguimiento.ver_Seguimiento')) 

@Seguimiento_bp.route("/eliminar/<int:id_cita>")
def eliminar(id_cita):
    col.delete_one({"id_cita": id_cita})
    return redirect(url_for('Seguimiento.ver_Seguimiento'))

@Seguimiento_bp.route("/editar/<int:id_cita>")
def editar(id_cita):
    cita = col.find_one({"id_cita": id_cita}, {'_id': 0})
    if not cita:
        return redirect(url_for('Seguimiento.ver_Seguimiento'))
    return render_template('formSeguimiento.html', cita=cita)

@Seguimiento_bp.route("/actualizar/<int:id_cita>", methods=["POST"])
def actualizar(id_cita):
    col.update_one(
        {"id_cita": id_cita},
        {"$set": {
            "paciente":   request.form.get("paciente"),
            "id_medico":  request.form.get("id_medico"),
            "fecha":      request.form.get("fecha"),
            "costo":      request.form.get("costo"),
            "estatus":    request.form.get("estado")
        }}
    )
    return redirect(url_for('Seguimiento.ver_Seguimiento'))