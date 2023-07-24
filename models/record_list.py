from operator import truediv
from re import T
from models.record import Record

records = [
    Record("How High", "Cogniac", "Disco", "12\"", True, "https://i.discogs.com/23yc9Kvr5VpOMqmZrrljDTrgywEKU37B_SAcgrMY_9Q/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTgxMDU1/OC0xMjM4NjEyMDI0/LmpwZWc.jpeg"),
    Record("I'm So Glad", "Earnie Burnside", "Gospel", "12\"", False, "https://i.discogs.com/uKelxd-9vJ15kkjADRsK1gvD6SDcZn0kcgKiOW7AIjk/rs:fit/g:sm/q:90/h:600/w:597/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTY2Mzkw/Ny0xMTQ1MDE0ODQy/LmpwZWc.jpeg"),
    Record("I Want You For Myself", "Dennis Rowland", "Boogie", "7\"", False, "https://i.discogs.com/-mg2jTFUgXzN-yDcOSN9nnZHPvcSgUldgBgq1KhD29Y/rs:fit/g:sm/q:90/h:383/w:394/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTE2NTk0/MDItMTIzNTEyOTcy/NS5qcGVn.jpeg"),
    Record("Mais Que Um Momento", "Emilio Santiago", "Latin", "LP", True, ""),
    Record("I Need Your Love", "Joy", "Boogie", "12\"", False, ""),
    Record("Love Is The Answer", "Jay Player", "Modern Soul", "12\"", False, ""),
    Record("A Step Ahead", "9th Creation", "Disco", "LP", True, ""),
    Record("The Power Of Love", "Wardell Piper", "Disco", "7\"", True, ""),
    Record("Only You", "Teddy Pendergrass", "Disco", "LP", True, ""),
    Record("Throw Down", "Carmen", "Boogie", "12\"", True, ""), 
    Record("Fallen Into Love", "Motherfox", "Disco", "12\"", True, ""), 
    Record("Just Loving You", "Judy Cheeks", "Northern Soul", "7\"", False, ""), 
    Record("Spirit Of The Living God", "Roslyn & Charles", "Gospel", "LP", False, ""),
    Record("Khemitry", "Khemitry", "Boogie", "LP", True, ""),
    Record("Find Your Love", "Mary Stevens", "Boogie", "12\"", False, "")
]

def add_new_media(media):
    records.append(media)

def delete_media(media):
    [records.remove(record) for record in records if record.title == media]

def update_media(media, change):
    for record in records:
        if record.title == media:
            record.checked_out = change