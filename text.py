import os
import dotenv
import pymongo

client = pymongo.MongoClient("mongodb+srv://ansh:ansh070708@cluster0.3akkk.mongodb.net/?retryWrites=true&w=majority")
dataBase = client["Score"];
collection = dataBase["passwords"];
for i in collection.find():
    try:
        print(i["fernetKey"])
    except:
        print(i)


