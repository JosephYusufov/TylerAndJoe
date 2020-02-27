from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime

client = MongoClient()
db = client.test
restaurants = db.restaurants
restaurants.delete_many({})

def findByZip(zip): 
        print(restaurants.find({"zip" : zip}))        
        #print(command) 


findByZip(1)     
#print(result)
# pprint(posts.find_one())
