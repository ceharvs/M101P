__author__ = 'chris_000'

import pymongo
import sys

connection = pymongo.MongoClient()

db = connection.pics

images = db.images
albums = db.albums

try:
    cursor_images = images.find()#{"_id":True, 'tags':True})
    albums_list = albums.aggregate([{"$group":
                                         {"_id":"list",
                                          "images":{"$addToSet":"$images"}}}])

except:
    print "Unexpected error:", sys.exc_info()[0]

sanity = 0
#print albums_list.keys()
result = albums_list['result'][0]
# print result['images']
new_list = []
for item in result['images']:
    new_list = new_list + item

print len(new_list)

new_list_2 = []

for doc in cursor_images:
    if doc['_id'] in new_list:
        new_list_2.append(doc['_id'])

print len(new_list_2)
for item in new_list_2:
    try:
        images.remove(item)
    except:
        print "Unexpected error:", sys.exc_info()[0]
