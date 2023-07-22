from operator import truediv
from re import T
from models.record import Record

records = [
    Record("How High", "Cogniac", "Disco", "12\"", True),
    Record("I'm So Glad", "Earnie Burnside", "Gospel", "12\"", False),
    Record("I Want You For Myself", "Dennis Rowland", "Boogie", "7\"", False),
    Record("Mais Que Um Momento", "Emilio Santiago", "Latin", "LP", True)
]

def add_new_media(media):
    records.append(media)

def delete_media(media):
    [records.remove(record) for record in records if record.title == media]