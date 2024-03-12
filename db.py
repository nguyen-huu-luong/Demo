from pymongo import MongoClient

uri = "mongodb+srv://nguyenhuuluong1204:nguyenhuuluong1204@cluster0.lasapro.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class DB:
    def __init__(self):
        connection = MongoClient(uri)
        self.db = connection["Demo"]
        
    def insert(self, collection, username, school, birthday):
        document = {"username": username, "school": school, birthday: birthday}
        try:
            self.db[collection].insert_one(document)
        except Exception as e:
            print("Error")
            
db_connection = DB()
    