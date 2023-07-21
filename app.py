from flask import Flask
from controllers.records_controller import records_blueprint

app = Flask(__name__)
app.register_blueprint(records_blueprint)

