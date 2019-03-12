import pymongo
import nltk


def connectToDB():
    myClient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    mydb = myClient["ir"]
    DocCol = mydb["docCollection"]
    return DocCol


def findMaxDocID(DocCol):
    x = DocCol.find_one()
    if(x != "none"):
        max = 0
        for doc in DocCol.find():
            if (doc['id'] > max):
                max = doc['id']
        return max + 1
    else:
        return 0


def Create_Doc_Index(doc):
    sentence_data = doc.read()
    nltk_tokens = nltk.word_tokenize(sentence_data)
    return nltk_tokens

def Insert_New_Doc_Record_to_DB(doc_metadata, docCollection):
    myquery = {
        "id": doc_metadata[3],
        "name": doc_metadata[0],
        "author": doc_metadata[1],
        "date_of_create": doc_metadata[2]
    }
    docCollection.insert_one(myquery)