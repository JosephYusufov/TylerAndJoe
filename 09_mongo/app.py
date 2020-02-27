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
        for restaurant in restaurants.find({"address.zipcode" : str(zip)}):
                print(restaurant)        

findByZip(10282)    
#print(result)
# pprint(posts.find_one())
