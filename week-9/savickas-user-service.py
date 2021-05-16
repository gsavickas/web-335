# Grayton Savickas WEB 335 May 16 2021

from pymongo import MongoClient
import pprint
import datetime
client = MongoClient('localhost', 27017)
db = client.web335
user = {
    "first_name": "Curtis",
    "last_name": "Lowe",
    "email": "addmelol@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))

pprint.pprint(db.users.find_one({"employee_id": "0000008"}))