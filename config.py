from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "21140176"))
API_HASH = environ.get("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "8476681745:AAEgPcnzKgSeL78a2fRwurfZrka5y70jPPY")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6222491731")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://sbmod88_db_user:XCLxrjdGlaHTG6mz@cluster0.qndjonz.mongodb.net/?appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
