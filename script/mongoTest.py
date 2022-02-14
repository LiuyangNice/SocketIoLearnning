import pymongo as mgdb


client = mgdb.MongoClient('mongodb://lyy:105014@mongoAuth:27017/lyy')

mydb = client["lyy"]
mycol = mydb["userinfos1"]
mycol.insert_one({"name":"lyy","password":"123123"})
x = mycol.find_one({"name":"lyy"})
if x is not None:
    print(x["password"])
    # mycol.delete_one(x)



