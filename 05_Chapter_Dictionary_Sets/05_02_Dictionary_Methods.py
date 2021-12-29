myDict = {"Harry": "A Coder", 
            "Heyan": "Eldest son",
            "Tejas": "Youngest Son",
            "Marks": "[1,2,5]",
            "AnotherDict": {"fruits": "Mango"},
            1:2
            }
'''            
#To find all the keys in the dictionary
print(myDict.keys())

#To find all the values in the dictionary
print(myDict.values())

#To check data type of a dictionary
print(type(myDict.keys()))
print(type(myDict.values()))

#To convert class dict to class list
print(list(myDict.keys()))
print(list(myDict.values()))

#To convert Dictionary into tuple so that you can iterate
print(myDict.items())

#To update disctionary by adding (keys:Values) or just values
print(myDict)
updateDict = {"Lovish":"Friend", "Heyan":"dancer"}
myDict.update(updateDict)
print(myDict)
'''
#why get method to use? *** The difference between .get() and [] syntax
print(myDict["Heyan"])
print(myDict.get("Heyan"))


print(myDict.get("Heyan2")) #Since Heyan2 is not available, it returns None
print(myDict["Heyan2"]) # Since Heyan2 is not available, it returns Error

