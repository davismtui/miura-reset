import pymongo



myclient = pymongo.MongoClient("mongodb://cosmos-db-free-02:ngB8oTzcNKlRtUiYq7y4wrlCgL08wM6UkFXxBqg0bwKAtCO4UUU2XNB0iQpFOstAqnDUZIqmZTCeACDbui7Ewg==@cosmos-db-free-02.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmos-db-free-02@")


def log(email, time):
    mydb = myclient["phishin"]


    mycol = mydb["email"]


    email_obj = {
      "email": email,
      "time": time

    }

    mycol.insert_one(email_obj)
