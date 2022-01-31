#
import pymongo

def mgdb(onedb, create=False, port=27017):
    myclient = pymongo.MongoClient('mongodb://127.0.0.1:' + str(port))
    mydb = myclient[onedb]
    if create:
        mydb.drop_database()
    return mydb


def mgcol(onedb, onecol, create=False, port=27017):
    mydb = mgdb(onedb, create=False, port=port)
    mycol = mydb[onecol]
    if create:
        mycol.drop()
    mycol = mydb[onecol]
    return mycol
