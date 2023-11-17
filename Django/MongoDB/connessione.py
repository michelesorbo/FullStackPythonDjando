
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://talent:corsopython2023@formatemp.tstbw70.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Vado a selezionare il DataBase da utilizzare
db = client['ecommerce'] #use ecommerce

#seleziono la collezione film
film_col = db['film']

print(film_col.find())

for film in film_col.find():
    print(film)