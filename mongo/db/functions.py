import json

def readJson(jsonName, path):
    print(path + jsonName +".json")
    with open( path + jsonName +".json", 'r') as outfile:
        jsonData = json.load(outfile)
    return jsonData

def writetoJson( jsonData, path, jsonName):
    with open(path + jsonName + ".json", 'w') as outfile:
            json.dump(jsonData, outfile)
            
def match(data, lhs, operator, rhs):
    #checking for "=" operator
    records = []
    for d in data:
        for key in data[d]:
            if lhs == key:
                if operator == '=':
                    if str(data[d][key]) == str(rhs):
                        records.append(int(d))
                    
            #checking for "<" operator
                elif operator == '<':                            
                    if int(data[d][key]) < int(rhs):
                        records.append(int(d))
                            
                            #checking for ">" operator
                elif operator == '>':
                     if int(data[d][key]) > int(rhs):
                         records.append(int(d))
    return records
                
            
