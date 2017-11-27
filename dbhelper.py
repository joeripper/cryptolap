import pymongo

from bson.objectid import ObjectId

DATABASE = "cryptolap"

class DBHelper:
    def __init__(self):
        client = pymongo.MongoClient()
        self.db = client[DATABASE]

    def get_user(self, email):
        return(self.db.users.find_one({"email": email}))

    def add_user(self, email, salt, hashed, pub_key, priv_key):
        self.db.users.insert({"email": email, "salt": salt, "hashed": hashed, "pub_key": pub_key, "priv_key": priv_key})

    def add_message(self, reciever, message, enc_message, owner):
        new_id = self.db.messages.insert({"message": message, "enc_message": enc_message, "owner": owner, "reciever": reciever})

    def get_pubkey(self, reciever):
        user = self.db.users.find_one({"email": reciever})
        return(user['pub_key'])

    def get_messages(self, owner_id):
        return(list(self.db.messages.find({"owner": owner_id})))

    def get_dashboard_messages(self, owner_id):
        return(list(self.db.messages.find({"reciever": owner_id})))


