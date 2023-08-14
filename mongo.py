from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from libs import env
uri = env.load('MONGODB_URI')
client = MongoClient(uri, server_api=ServerApi('1'))

print('Connecting to DB...')
try:
    client.admin.command('ping')
    print("successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.WMSGPT
collection = db.user_list

# 컬렉션에서 모든 문서를 조회합니다.
for doc in collection.find():
    print(doc)
