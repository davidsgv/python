from flask import Blueprint, render_template
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