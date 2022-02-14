import pymongo as mgdb


client = mgdb.MongoClient('mongodb://lyy:105014@127.0.0.1:20000')

mydb = client["server"]
mycol = mydb["userinfos1"]
mycol.insert_one({"name":"lyy","password":"123123"})
x = mycol.find_one({"name":"lyy"})
if x is not None:
    print(x["password"])
    # mycol.delete_one(x)



