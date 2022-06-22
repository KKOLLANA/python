import pymongo  #import the package

client=pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb=client['Employee'] #With this it will not create the databaste till we create the collections

information=mydb.employeeinformation #employeeinformation is a collection or table name here
record={
    'firstname':'kiran',
    'lastname':'kollana',
    'department':'MCA'

}
information.insert_one(record)