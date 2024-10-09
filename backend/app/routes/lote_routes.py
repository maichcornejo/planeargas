# backend/app/routes/lote_routes.py
from flask import Blueprint, request, jsonify
from app.main.python.lote_service import crear_lote, obtener_lote


lote_bp = Blueprint('lote', __name__)

@lote_bp.route('/lote', methods=['POST'])
def crear_nuevo_lote():
    try:
        print("Recibiendo solicitud de creación de lote")
        data = request.json
        print(f"Datos recibidos: {data}")
        
        # Validar si ya existe un lote con la misma calle y altura
        lote_existente = obtener_lote(data['nombre_calle'], data['altura'])
        if lote_existente:
            print("Lote ya existe")
            return jsonify({"message": "El lote ya existe"}), 400

        # Crear el nuevo lote
        print("Creando nuevo lote")
        nuevo_lote = crear_lote(data)
        print(f"Lote creado con ID: {nuevo_lote.id}")
        
        return jsonify({"message": "Lote creado con éxito", "id": nuevo_lote.id}), 201
    except Exception as e:
        print(f"Error: {e}")  # Imprime el error en los logs
        return jsonify({"error": str(e)}), 500  # Devuelve el error con un código 500
