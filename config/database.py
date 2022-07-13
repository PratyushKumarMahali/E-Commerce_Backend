from pymongo import MongoClient

# database url connects to the api with mongodb
# copy and paste the url below in compass to access the database
mongodb_uri = 'mongodb+srv://zemusi:234892@cluster2.v0hbs.mongodb.net/?retryWrites=true&w=majority'
port = 8000
client = MongoClient(mongodb_uri, port)
db = client["TE13"]