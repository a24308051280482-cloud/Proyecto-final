from flask import Blueprint, render_template, request, redirect, url_for
from database import db

Medicos_bp = Blueprint('Medicos', __name__)
col = db['Medicos']

@Medicos_bp.route("/")
def ver_Medicos():
    lista = list(col.find({}, {'_id': 0}))
    return render_template('Medicos.html', doctores=lista)

@Medicos_bp.route("/nuevo")
def formulario():
    return render_template('formMedicos.html')

@Medicos_bp.route("/guardar", methods=["POST"])
def guardar():
    ultimo = col.find_one({"id_doctor": {"$type": "int"}}, sort=[("id_doctor", -1)])
    nuevo_id = (ultimo["id_doctor"] + 1) if ultimo else 1

    col.insert_one({
        "id_doctor":        int(nuevo_id),
        "nombre":           request.form.get("nombre"),
        "especialidad":     request.form.get("especialidad"),
        "edad":             int(request.form.get("edad")),
        "sexo":             request.form.get("sexo"),
        "telefono":         request.form.get("telefono"),
        "Tipo_de_sangre":    request.form.get("Tipo_de_sangre"),
        "turno":            request.form.get("turno"),
    })
    return redirect(url_for('Medicos.ver_Medicos'))

@Medicos_bp.route("/eliminar/<int:id_doctor>")
def eliminar(id_doctor):
    col.delete_one({"id_doctor": id_doctor})
    return redirect(url_for('Medicos.ver_Medicos'))

@Medicos_bp.route("/editar/<int:id_doctor>")
def editar(id_doctor):
    doctor = col.find_one({"id_doctor": id_doctor}, {'_id': 0})
    if not doctor:
        return redirect(url_for('Medicos.ver_Medicos'))
    return render_template('formMedicos.html', doctor=doctor)

@Medicos_bp.route("/actualizar/<int:id_doctor>", methods=["POST"])
def actualizar(id_doctor):
    col.update_one(
        {"id_doctor": id_doctor},
        {"$set": {
            "nombre":           request.form.get("nombre"),
            "especialidad":     request.form.get("especialidad"),
            "edad":             int(request.form.get("edad")),
            "sexo":             request.form.get("sexo"),
            "telefono":         request.form.get("telefono"),
            "Tipo_de_sangre":    request.form.get("Tipo_de_sangre"),
            "turno":            request.form.get("turno"),
        }}
    )
    return redirect(url_for('Medicos.ver_Medicos'))