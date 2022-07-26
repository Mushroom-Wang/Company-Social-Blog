from kittencompanyblog.error_pages.handlers import error_pages
from kittencompanyblog.core.views import core
from flask import Flask

app = Flask(__name__)

app.register_blueprint(core)

app.register_blueprint(error_pages)
