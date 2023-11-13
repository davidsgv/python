from flask import Flask
from application.controller.producto import router

app = Flask(__name__)
app.register_blueprint(router)
