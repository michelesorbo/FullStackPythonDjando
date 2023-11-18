
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

#print(film_col.find())

# for film in film_col.find():
#     print(film)

#Se voglio solo il primo docuemnto della collection
#print(film_col.find_one({'titolo':'Alien'}))

#Utilizzo la collezione prodotti
prod_col = db['prodotti']

#Voglio cercare tutti i prodotti che hanno una quantità
for p in prod_col.find({"quantita": {"$gt": 10}}):
    # print(type(p))
    # print(p.keys())
    # print(p.values())
    for k,v in p.items():
        print(f'{k} : {v}')
    print('\n\n')

#Inserisco un nuovo film
# film = {
#     'titolo':'Avatar',
#     'anno': '2010',
#     'genere': 'Fantasy'
# }

# esito = film_col.insert_one(film)
# print(f'Elemento inserito id: {esito.inserted_id}')

films = [
    {'titolo':'The Boys', 'genere':'Serire TV', 'streaming':'Amazon'},
    {'titolo':'Attacco dei giganti', 'genere':'Anime', 'nazionalita':'Giapponese','streaming': ['Amazon','Netflix']}
]

ris = film_col.insert_many(films)
print(f'Elemento inserito id: {ris.inserted_ids}')