# Grayton Savickas WEB 335 May 16 2021


from pymongo import MongoClient
import pprint
import datetime
client = MongoClient('localhost', 27017)

db = client.web335

result = db.users.delete_one({
    "first_name": "Curtis",
    "last_name": "Lowe",
    "email": "addmelol@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
})
print(result)
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))