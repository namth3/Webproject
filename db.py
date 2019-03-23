from flask_pymongo import PyMongo
import app as s

s.app.config['MONGO_DBNAME'] = 'db_name'
s.app.config['MONGO_URI'] = "mongodb+srv://namth3:MN1Cbt6BFOvUIExD@cluster0-kondi.mongodb.net/test?retryWrites=true"

mongo = PyMongo(s.app)