from db.functions import readJson
from db.functions import writetoJson
class Records():
    """docstring for document."""
    def __init__(self, db_name, collection_name):
        self.db_name = db_name
        self.collection_name = collection_name
        # loading config .json file
        pathJson = readJson("config" , "")
        self.path = pathJson['path']
        self.db_path = self.path + "/"  + self.db_name + "/"
        
        #load colelction
        self.jsonData = readJson(self.collection_name , self.db_path) 
        print (self.jsonData)
        self.__cretaeRecord()
    
    def __cretaeRecord(self):
                #variables
        self.list1 = []
        self.table = {}
        
        #creating id for appending
        if self.jsonData=={}:
            self.maxi = 0
        else:
            for self.key in self.jsonData:
                self.list1.append(int(self.key))
            self.maxi = max(self.list1)
        #while loop for updating the columns
        while True:
            self.table_attr = input("Enter the attribute for a table : ").lower()
            self.attr_val = input("Enter the value to attribute : ")
            if self.table_attr == "" and self.attr_val == "":
                break
            self.table[self.table_attr] = self.attr_val
        self.jsonData[self.maxi + 1] = self.table
        #dumping collection into json file
        writetoJson(self.jsonData, self.db_path, self.collection_name)
        
        