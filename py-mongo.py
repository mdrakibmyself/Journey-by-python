from pymongo import MongoClient

# 1. Connect to your local MongoDB or MongoDB Atlas instance
# Local example: "mongodb://localhost:27017"
# Atlas example: "mongodb+srv://<user>:<password>@cluster.mongodb.net/"
client = MongoClient("mongodb://localhost:27017")

# 2. Access a database (use dictionary or dot notation)
db = client["my_ecommerce_db"]
# Alternative: db = client.my_ecommerce_db

# 3. Access a collection (equivalent to a table in SQL)
products = db["products"]
