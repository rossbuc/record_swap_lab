from flask import Blueprint, render_template
from models.record_list import records

records_blueprint = Blueprint("records", __name__)

@records_blueprint.route('/records')
def index():
    return render_template("index.jinja", title="Media List", record_list=records)

@records_blueprint.route('/records/<name>')
def record(name):
    record = [record for record in records if record.title == name]
    return render_template("record.jinja", title=name, record=record[0])