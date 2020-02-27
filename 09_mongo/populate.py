from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime

client = MongoClient()
db = client.test
restaurants = db.restaurants
restaurants.delete_many({})

with open("./primer-dataset.json", 'r') as file:
    data = json.load(file)
    for member in data:
        id = restaurants.insert_one(loads(json.dumps(member)))
        print(id)

def findByZip(zip): 
        print(restaurants.find({"zip" : zip}))        
        #print(command) 


findByZip(1)     
#print(result)
# pprint(posts.find_one())
