from flask import Blueprint, render_template, redirect, url_for, request
from application.model.producto import Producto

producto = Producto()
router = Blueprint('app', __name__)

@router.route("/")
def index():
    data = producto.get_productos()
    return render_template('index.html', productos=data)

@router.route("/producto")
def producto_page():
    data = producto.get_productos()
    return render_template('productos.html', productos=data)

#formularios
@router.route("/producto/crear/", methods = ['GET', 'POST'])
def producto_crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['imagen']

        producto.add_producto(nombre,imagen,precio)
        return redirect(url_for('app.producto_page'))
    return render_template('formulario.html')

@router.route("/producto/editar/<int:id>", methods = ['GET', 'POST'])
def producto_editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['imagen']

        producto.update_producto(id,nombre,imagen,precio)
        return redirect(url_for('app.producto_page'))
    
    data = producto.get_by_id(id)
    return render_template('formulario.html', producto=data)

#borrar
@router.route("/producto/delete/<int:id>", methods = ['GET'])
def producto_delete(id):
    producto.delete_producto(id)
    return redirect(url_for('app.producto_page'))