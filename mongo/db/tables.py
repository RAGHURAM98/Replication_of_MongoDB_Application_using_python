
from db.records import Records
from db.functions import readJson, writetoJson, match

#collection as object
class collections(object):
    """docstring for collections."""
    def __init__(self, dbName, metaData, collectionName):
        self.dbName = dbName
        self.metaData = metaData
        self.collectionName = collectionName
        self.data1 = {}
        self.data = {}
        
        #config.json as file
        pathJson = readJson("config" , "")
        self.path = pathJson['path']
        self.dbPath = self.path + "/"  + self.dbName + "/"
        
        while True:
            choice = input("""
                           -----------------
                           1 for __createDocument
                           2 for delete_document
                           3 display document
                           4 Update document
                           5 Exit
                           --------""")
            
            #create the document
            if choice == "1":
                self.__createDocument()
            
            #delete the record
            elif choice == "2":
                self.__deleteRecord(self.collectionName)
            
            #show the reocrds
            elif choice == "3":
                choices = input(""" 
                              -------------------
                              1 for showing all the records
                              2 for showing the records on conditon
                              -------------------""" )
                if choices == "1":
                    self.__showRecords(self.collectionName)
                    
                elif choices == "2":
                    self.__ShowRecord(self.collectionName)
                    
                else:
                    print("Invalid . enter valid choice")
                    continue
            
            #update records
            elif choice == "4":
                self.__UpdateRecord(self.collectionName)
                
            #break the while loop
            elif choice == "5":
                break
            
            else:
                print("Invalid . enter valid choice")
                continue
    
    #show all the records        
    def __showRecords(self, collName):
        self.collName = collName
        #load json file as read
        self.data = readJson(self.collName , self.dbPath) 
        print(self.data)
    
    #show the record 
    def __ShowRecord(self, collName):
        self.collName = collName
        self.data = readJson(self.collName , self.dbPath) 
        print(self.data)
        self.lhs = input("Enter attr : ").lower()
        self.operator = input("Enter opp : ")
        self.rhs = input("Enter val : ")
       
        
        self.records = match(self.data, self.lhs, self.operator, self.rhs)               
                            
        #print the data
        if self.records:
            for self.key in self.records:
                print(self.data[str(self.key)])
        else:
            print("Please check attributes in databases")

    #create document
    def __createDocument(self):
        while True:
            self.flag = input("Create a document ? Enter 'y' ").lower()
            if self.flag == 'y':
                #calling records class
                Records(self.dbName, self.collectionName)
            else:
                break
    
    #delete record
    def __deleteRecord(self, collName):
        self.collName = collName
        self.updatedRecords = {}
        self.records = []

        self.data = readJson(self.collName , self.dbPath) 

        self.lhs = input("Enter attr : ").lower()
        self.operator = input("Enter opp : ")
        self.rhs = input("Enter val : ")
        
        self.records = match(self.data, self.lhs, self.operator, self.rhs)               
        #print daata
        if self.records:
            for self.key in self.records:
                self.data.pop(str(self.key))
            self.counter = 1
            print(self.data)
            for self.key in self.data:
                self.updatedRecords[str(self.counter)] = self.data[str(self.key)]
                self.counter += 1
            print(self.updatedRecords)
            #dumping collection into json file
            writetoJson(self.updatedRecords, self.dbPath, self.collName)
        else:
            print("Please check attributes in databases")      
        
        
            
    #update record
    def __UpdateRecord(self, collName):
        self.collName = collName
        self.records = []

        self.data = readJson(self.collName , self.dbPath) 

        self.lhs = input("Enter attr : ").lower()
        self.operator = input("Enter opp : ")
        self.rhs = input("Enter val : ")
        self.upAttr = input("Attr to be updated : ").lower()
        self.upVal = input("Value to be updated : ")

        self.records = match(self.data, self.lhs, self.operator, self.rhs)               
        for self.key in self.records:
            self.data[str(self.key)][self.upAttr] = self.upVal

        print("values after updation : ", self.data)
        writetoJson(self.data, self.dbPath, self.collName)
