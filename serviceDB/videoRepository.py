from pymongo import MongoClient


class DataBaseConnection:
    def __init__(self, database_name="my_database", collection_name="my_collection"):
        self.MONGO_URI = "mongodb://127.0.0.1:27017/"
        self.DATABASE_NAME = database_name
        self.COLLECTION_NAME = collection_name
        try:
            self.client = MongoClient(self.MONGO_URI)
            self.db = self.client[self.DATABASE_NAME]
            self.collection = self.db[self.COLLECTION_NAME]
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def insert_videos(self, videos):
        try:
            for vid in videos:
                self.collection.insert_one(vid.to_dict())
                print(f"Inserted video: {vid.cod}")

            print("-- DATA LOADED SUCCESSFULLY --")
        except Exception as e:
            print(f"Error inserting videos: {e}")

    def close(self):
        if self.client:
            self.client.close()

