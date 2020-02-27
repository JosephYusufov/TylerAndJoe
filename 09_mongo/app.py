from pymongo import MongoClient
from pprint import pprint
from bson.json_util import loads
import json
import datetime

client = MongoClient()
db = client.test
restaurants = db.restaurants


def findByZip(zip): 
        for restaurant in restaurants.find({"address.zipcode" : str(zip)}):
                print(restaurant)        

    
def findByBorough(borough):
    for restaurant in restaurants.find({"borough": borough}):
        pprint(restaurant)

        
def findByZipWithScoreCap(zip, score):
    # for restaurant in 

def findByZipAndScore(zip, score):
        for restaurant in restaurants.find({"address.zipcode" : str(zip), "grades.score": {"$lt": score}}):
                print(restaurant["name"]) 
        
findByZip(1)
findByBorough("Bronx")
# print(result)
# pprint(posts.find_one())
