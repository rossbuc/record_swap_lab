from flask import Blueprint, render_template, request, redirect
from models.record_list import records, Record, add_new_media, delete_media

records_blueprint = Blueprint("records", __name__)

@records_blueprint.route('/records')
def index():
    return render_template("index.jinja", title="Media List", record_list=records)

@records_blueprint.route('/records/<name>')
def record(name):
    record = [record for record in records if record.title == name]
    return render_template("record.jinja", title=name, record=record[0])

@records_blueprint.route('/records', methods=['POST'])
def add_record():
    record_title = request.form['title']
    record_artist = request.form['artist']
    record_genre = request.form['genre']
    record_format = request.form['format']
    record_to_add = Record(record_title, record_artist, record_genre, record_format)
    add_new_media(record_to_add)
    return redirect('/records')

@records_blueprint.route('/records/delete/<index>', methods=['POST'])
def delete_record(index):
    record_title_to_delete = request.form['title_to_delete']
    delete_media(record_title_to_delete)
    return redirect('/records')
