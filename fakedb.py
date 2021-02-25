import pymongo
import model

client = pymongo.MongoClient('localhost',27017)
db = client.Meetings
meet_data = {}
