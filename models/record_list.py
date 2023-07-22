from operator import truediv
from re import T
from models.record import Record

records = [
    Record("How High", "Cogniac", "Disco", "12\"", True),
    Record("I'm So Glad", "Earnie Burnside", "Gospel", "12\"", False),
    Record("I Want You For Myself", "Dennis Rowland", "Boogie", "7\"", False),
    Record("Mais Que Um Momento", "Emilio Santiago", "Latin", "LP", True),
    Record("I Need Your Love", "Joy", "Boogie", "12\"", False),
    Record("Love Is The Answer", "Jay Player", "Modern Soul", "12\"", False),
    Record("A Step Ahead", "9th Creation", "Disco", "LP", True),
    Record("The Power Of Love", "Wardell Piper", "Disco", "7\"", True),
    Record("Only You", "Teddy Pendergrass", "Disco", "LP", True),
    Record("Throw Down", "Carmen", "Boogie", "12\"", True), 
    Record("Fallen Into Love", "Motherfox", "Disco", "12\"", True), 
    Record("Just Loving You", "Judy Cheeks", "Northern Soul", "7\"", False), 
    Record("Spirit Of The Living God", "Roslyn & Charles", "Gospel", "LP", False),
    Record("Khemitry", "Khemitry", "Boogie", "LP", True),
    Record("Find Your Love", "Mary Stevens", "Boogie", "12\"", False)
]

def add_new_media(media):
    records.append(media)

def delete_media(media):
    [records.remove(record) for record in records if record.title == media]

def update_media(media, change):
    for record in records:
        if record.title == media:
            record.checked_out = change