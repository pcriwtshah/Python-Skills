story = "once upon a time there was a youtuber named Harry who uploaded python course with notes. he is very good."
print(story)
print(len(story)) #gives length of character
print(story.endswith("notes")) #gives true or false
print(story.count("a")) #count the number of times "a" appears in story.
print(story.count("er"))
print(story.count(" "))
print(story.capitalize()) # Capitalize only the first character.
print(story.find("Harry")) #Find the location it is at 44 index
print(story.find("a")) # gives only first location. if it is not found, then it returns -1
print(story.replace("Harry", "Divya")) #replaces all old word with new word 

#Find double spaces in a string
st = "This is a string with   double spaces"
doublespaces = st.find("  ")
print(doublespaces)

st_updated = st.replace("   ", " ")
print(st_updated)