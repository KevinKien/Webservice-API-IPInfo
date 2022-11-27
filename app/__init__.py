from flask import Flask, render_template, Blueprint, jsonify, session
from flask_wtf.csrf import CSRFProtect
import jinja2

class MyApp(Flask):
  def __init__(self):
    Flask.__init__(self, __name__)
    self.jinja_loader = jinja2.ChoiceLoader([self.jinja_loader,jinja2.PrefixLoader({}, delimiter = ".")])
    def create_global_jinja_loader(self):
        return self.jinja_loader

    def register_blueprint(self, bp):
        Flask.register_blueprint(self, bp)
        self.jinja_loader.loaders[1].mapping[bp.name] = bp.jinja_loader

app = MyApp()
app.config['SECRET_KEY'] = '5ebe2294ecd0e0f08eab7690d2a6ee69'
csrf = CSRFProtect(app)

from app.routes import *
from app.api import *

