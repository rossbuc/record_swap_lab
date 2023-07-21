from flask import Blueprint, render_template
from models.record_list import records

records_blueprint = Blueprint("records", __name__)

@records_blueprint.route('/records')
def index():
    return render_template("index.jinja", title="Media List", record_list=records)