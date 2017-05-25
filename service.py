import json
import pymongo
from bottle import request, route, run


@route('/',method='POST')
def index():

     # getting data
     data=request.params.get('data')
     print ('your data = {data}'.format(data))

     # establish a connection to the database
     connection = pymongo.MongoClient("mongodb://localhost")

     # get a handle to the bigdata
     db = connection.bigdata
     sensor = db.sensor


     # insert data
     try:
         sensor.insert_one(data)
     except Exception as e:
         print ("Unexpected error: {}",format(type(e)))

     return "sucess"

run(host='0.0.0.0', port=8080, debg=True)
