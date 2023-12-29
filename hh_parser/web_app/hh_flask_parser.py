
import sys
import os
import unittest
import json
sys.path.append(os.path.join(os.getcwd(), '..'))
import multiprocessing as ml
from parser_app import main as pr
#from web_app import create_app

from flask import Flask, render_template

SECRET_KEY = b'\x143#\x1eV;\xc9\xa0\xecr\r\xd4/{b\n'

app = Flask(__name__)
app.config.from_object(__name__)

def create_app():
    from hh_parser.web_app.flask_parser.flask_parser import parser_blueprint
    from hh_parser.web_app.authorization.auth import auth_blueprint
    app.register_blueprint(parser_blueprint)
    app.register_blueprint(auth_blueprint)

    return app


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    # Создать приложение Flask
    app = create_app()

    # Запустить парсер
    par_service = ml.Process(name="HH Parser", target=pr.main)
    par_service.start()


    # Запустить Flask приложение
    app.run()
