from flask import Blueprint, request, jsonify
from app.main.python.plano_service import crear_plano

plano_bp = Blueprint('plano', __name__)

@plano_bp.route('/nuevo-plano', methods=['POST'])
def cargar_plano():
    try:
        # Recoger los datos del formulario
        data = {
            'artefactos': request.form['artefactos'],
            'material': request.form['material'],
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'matricula': request.form['matricula'],
            'categoria': request.form['categoria']
        }

        # Recoger los archivos adjuntos
        credencial = request.files.get('credencial')
        planta = request.files.get('planta')

        # Llamar al servicio para crear el nuevo plano
        nuevo_plano = crear_plano(data, credencial_file=credencial, planta_file=planta)

        return jsonify({"message": "Plano cargado con éxito", "plano_id": nuevo_plano.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
