#Create a Dictionary
myDict = {"Harry": "A Coder", 
            "Heyan": "Eldest son",
            "Tejas": "Youngest Son",
            "Marks": "[1,2,5]",
            "AnotherDict": {"fruits": "Mango"}
            }
#Look the values of keys (keyword)
print(myDict["Harry"])
print(myDict["Marks"])
print(myDict['AnotherDict'])
print(myDict['AnotherDict']['fruits'])

#Properties of Dictionary
#It is unordered, mutable, indexed, no duplicate keys

#Change the value of keys
myDict['Marks'] = [9, 8, 7]
print(myDict['Marks'])
print(myDict)
'''
#Let the user see te meaning/values of the keys (Keyword)
print("Options are ", myDict.keys())
a = input("Enter the word: ")
#print("The values/meaning of your word is ", myDict[a]) #This will show error if user input word that is not in the dictionary
#To avaoid error
print("The values/meaning of your word is ", myDict.get(a)) #This will show None instead of error
'''

#User input Dictionary
favLang = {}
a = input("Enter your favorite language Shivam: \n")
b = input("Enter your favorite language Shivani: \n")
c = input("Enter your favorite language Shiv: \n")
d = input("Enter your favorite language Shivendra: \n")
favLang['Shivam'] = a
favLang['Shivani'] = b
favLang['Shiv'] = c
favLang['Shivendra'] = d
print(favLang)
