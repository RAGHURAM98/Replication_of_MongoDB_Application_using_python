import os
import shutil

from db.db import Database
from db.functions import readJson
    
#loading the path to create a database folder

pathJson = readJson("config" , "")
path = pathJson['path']

# infinite loop to create multiple databases and ipulate  dbs 
while True:
    if not os.path.isdir(path):
        print(""" Invalid Path. Please update the 'path' field in config.json""")
        break
    #input the choice
    choice = input("""
                       -----------------
                       1. Create database 
                       2. Connect to database
                       3. delete database
                       4. Display databases
                       5. exit
                       -------------\n""")
    # creating db
    if choice == "1":        
        dbName = input("Enter database to create ").lower()
        try:
            if dbName in os.listdir(path):
                print("---- DB already exists ---- connecting to the database")
                try:
                    dbPath = path + "/"  + dbName + "/"
                    myJson = readJson("_metadata", dbPath)
                    userName = input("Enter userName : ").lower()
                    passwd = input("Enter passwd : ")

                    myDb = Database(dbName, userName, passwd, myJson)
                except:
                    print("database doesn't exists")
                
            elif dbName == "":
                print("Please enter a valid database name")
                
            else:
                defaultSettings = input("Enter 'y' to continue with defaults : ")
                os.mkdir(path + "/" + dbName)
            
                # creating db with defaultSettings
                if defaultSettings == 'y':
                    myDb = Database(dbName)
        
                # creating db with given userName and passwd
                else:
                    userName = input("Enter userName : ").lower()
                    passwd = input("Enter passwd : ")
                    myDb = Database(dbName, userName, passwd)
        except:
            print("pls give a proper database name ")
    
    # connecting to db
    elif choice == "2":
        try:
            dbName = input("Enter db to connect ").lower()
            dbPath = path + "/"  + dbName + "/"
            myJson = readJson("_metadata", dbPath)
            userName = input("Enter userName : ").lower()
            passwd = input("Enter passwd : ")
            dbPath = path + "/"  + dbName + "/"
            myJson = readJson("_metadata", dbPath)
            myDb = Database(dbName, userName, passwd, myJson)
        except:
            print("database doesn't exists")
    #delete the db
    elif choice == "3":
        try:
            dbName = input("Enter db to delete ").lower()
            dbPath1 = path + "/"  + dbName +"/"
            #load metadata for checking the username and password
            myJson = readJson("_metadata", dbPath1)
            userName = input("Enter userName : ").lower()
            passwd = input("Enter passwd : ")
            if myJson["userName"] == userName and myJson["passwd"] == passwd:
                shutil.rmtree(dbPath1)
                print("database deleted")
            else:
                print("password or user name is incorrect")
        except:
            print("no database is there to delete")
    #list the directoies       
    elif choice == "4":
        dbPath2 = path + "/" 
        print(os.listdir(dbPath2))
        
    #break for 5   
    elif choice == "5":
        break
    
    else:
        print("Invalid- please enter valid choice")
        continue