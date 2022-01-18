import pymongo as mgdb

client = mgdb.MongoClient("localhost",27017)
mydb  = client["runoobdb"]
mycol = mydb["sites"]
# mycol.insert_one({"name":"lyy","password":"123123"})
x = mycol.find_one({"name":"lyy"})
if  x is not None:
    print(x["password"])


