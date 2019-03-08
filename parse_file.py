import pymongo

def connectToDB():
    myClient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myClient["ir"]
    DocCol = mydb["docCollection"]
    return DocCol


def findMaxDocID(DocCol):
    max = 0
    for doc in DocCol.find():
        if (doc['doc_id'] > max):
            max = doc['doc_id']
    return max + 1