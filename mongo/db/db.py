import time
import os
from datetime import date
import re

from db.tables import collections
from db.functions import readJson,writetoJson

# Database is the object
class Database(object):
    def __init__(self, dbName, userName = "root", passwd = "123", data = None):
        self.data = data
        self.dbName = dbName
        self.userName = userName
        self.passwd = passwd
        self.metaData = data
        print("met : " , self.metaData)
        if self.data == None:
            #metadata file
            self.metaData = {"dbName" : self.dbName,
                             "userName" : self.userName,
                             'passwd' : self.passwd,
                             'time' : time.localtime(),
                             'date' : date.today().isoformat(),
                             'collection': []
                             }
            
            #loading config.json file
            pathJson = readJson("config" , "")
            self.path = pathJson['path']
            
            #dumping metadata file with values
            self.dbPath = self.path + "/"  + self.dbName + "/"
            writetoJson(self.metaData, self.dbPath,"_metadata")
            # for creating collection
            self.__createCollection()

        # creating db with given username and passwd
        elif self.userName == None and self.passwd == None:
            self.userName = "root"
            self.passwd = '123'
            self.__init__(self, self.dbName, self.userName , self.passwd)

        # for connecting to db
        else:
            self.data = data 
            self.dbUserName = self.data["userName"]
            self.dbPasswd = self.data["passwd"]
                        
            # checking whether the username and password are right or wrong
            if self.dbUserName == self.userName and self.dbPasswd == self.passwd:
                print("---- Connection established ----")
                #loading config.json file
                pathJson = readJson("config" , "")
                self.path = pathJson['path']
            
                #dumping metadata file with values
                self.dbPath = self.path + "/"  + self.dbName + "/"
                self.__createCollection()
            else:
                print("Incorrect username or passwd")
    
    #create colelction
    def __createCollection(self):
        while True:
            
            choice = input("""
                           -------------
                           1 create collection
                           2 delete collection
                           3 Display collection 
                           4 Exit db
                           --------------""")
            
            #create the colelction 
            if choice == "1":
                self.dataInit = {}
                self.collectionName = input("Enter collection name to be created : ")
                if re.search("^[a-zA-Z0-9]",self.collectionName):
                    if self.collectionName not in self.metaData['collection']:
                        writetoJson(self.dataInit,self.dbPath,self.collectionName)
                        
                        #new colelction name is append to collection list in metadata
                        self.metaData['collection'].append(self.collectionName)
                   
                        writetoJson(self.metaData,self.dbPath,"_metadata")
                        
                        #creating collections
                        collections(self.dbName, self.metaData, self.collectionName)
    
                    else:
                        self.collectionName1 = self.collectionName
                        collections(self.dbName, self.metaData, self.collectionName1)
                        print("-- collection exists --")
                else:
                    print ("collection name should not be empty")
            #to manpulate on existing collection
            
                
            
            #2 for delete the colelction
            elif choice == "2":
                self.collName = input("Enter collection to be deleted : ")
                self.__deleteCollection(self.collName)
            
            #3 for Display collection
            elif choice == "3":
                readJson("_metadata",self.dbPath)
                print(self.metaData['collection'])
        
            #for break
            elif choice == "4":
                break
            else:
                print("Inavlid Choice- enter a valid choice")
                continue

    #delete colelction
    def __deleteCollection(self, collectionName):
        try:
            self.collName = collectionName
                
            self.metaData=readJson("_metadata",self.dbPath)
                
            #removing the collection name and dumping the metadata
            self.metaData['collection'].remove(self.collName)
            
            writetoJson(self.metaData,self.dbPath,"_metadata")
            
            #removes collection file from db
            os.remove(self.path + self.collName + ".json")
        except:
            print("no collection exists to delete")
