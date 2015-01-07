import bottle
import pymongo

@bottle.route('/')
def index():
    #connect to mongoDB
    connection = pymongo.MongoClient('localhost',27017)

    #attach to a test database
    db = connection.test

    #get handle for names collection
    names = db.names

    #find a single document
    item = names.find_one()

    return'<b> Hello %s!</b>' % item['name']

bottle.run(host='localhost',port=8082)