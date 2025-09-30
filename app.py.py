import os
from datetime import datetime
from itertools import zip_longest
from urllib.parse import quote
from flask import Flask, render_template, request, redirect, url_for, flash, Response

import database
from pricing import calcular_precio

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-only-change-in-production')

# Configuración para producción
if os.environ.get('FLASK_ENV') == 'production':
    app.config['DEBUG'] = False
else:
    app.config['DEBUG'] = True

# Inicializar base de datos al arrancar
database.crear_bd()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boletas')
def boletas():
    todas_boletas = database.obtener_boletas()
    return render_template('boletas.html', boletas=todas_boletas)

@app.route('/boleta/nueva')
def boleta_nueva():
    return render_template('boleta_nueva.html')

@app.route('/crear_boleta', methods=['POST'])
def crear_boleta():
    try:
        # Obtener datos del formulario
        cliente = request.form.get('cliente', '').strip()
        telefono = request.form.get('telefono', '').strip()
        
        # Validaciones básicas
        if not cliente:
            flash('El nombre del cliente es obligatorio', 'error')
            return redirect(url_for('boleta_nueva'))
        
        # Obtener servicios (pueden ser múltiples)
        servicios = []
        cantidades = []
        
        # Recopilar todos los servicios del formulario
        for key in request.form.keys():
            if key.startswith('servicio_'):
                idx = key.split('_')[1]
                servicio = request.form.get(f'servicio_{idx}')
                cantidad = request.form.get(f'cantidad_{idx}', '0')
                
                if servicio and servicio != '' and int(cantidad) > 0:
                    servicios.append(servicio)
                    cantidades.append(int(cantidad))
        
        if not servicios:
            flash('Debe agregar al menos un servicio', 'error')
            return redirect(url_for('boleta_nueva'))
        
        # Crear la boleta en la base de datos
        boleta_id = database.crear_boleta_completa(cliente, telefono, servicios, cantidades)
        
        if boleta_id:
            flash('Boleta creada exitosamente', 'success')
            return redirect(url_for('ver_boleta', boleta_id=boleta_id))
        else:
            flash('Error al crear la boleta', 'error')
            return redirect(url_for('boleta_nueva'))
            
    except Exception as e:
        flash(f'Error al procesar la boleta: {str(e)}', 'error')
        return redirect(url_for('boleta_nueva'))

@app.route('/boleta/<int:boleta_id>')
def ver_boleta(boleta_id):
    try:
        # Obtener datos de la boleta
        cab = database.obtener_cabecera_boleta(boleta_id)
        items = database.obtener_items_boleta(boleta_id)
        
        if not cab:
            flash('Boleta no encontrada', 'error')
            return redirect(url_for('boletas'))
        
        return render_template('boleta_detalle.html', cab=cab, items=items)
        
    except Exception as e:
        flash(f'Error al cargar la boleta: {str(e)}', 'error')
        return redirect(url_for('boletas'))

@app.route('/boleta/<int:boleta_id>/imprimir')
def imprimir_boleta(boleta_id):
    try:
        cab = database.obtener_cabecera_boleta(boleta_id)
        items = database.obtener_items_boleta(boleta_id)
        
        if not cab:
            return "Boleta no encontrada", 404
        
        # Renderizar template para impresión
        html = render_template('boleta_detalle.html', cab=cab, items=items, imprimir=True)
        return Response(html, mimetype='text/html')
        
    except Exception as e:
        return f"Error: {str(e)}", 500

# Rutas para PWA
@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

@app.route('/sw.js')
def service_worker():
    return app.send_static_file('sw.js')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error="Página no encontrada"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error="Error interno del servidor"), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])