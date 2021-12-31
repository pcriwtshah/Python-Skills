#This program will find and replace the word in a file
with open('09_01_poem.txt') as f:
    data = f.read()

data = data.replace('twinkle', 'Twinkle')
data = data.replace('Hills', 'World')
#if 'Twinkle' in data:
#    pass

with open('09_01_poem.txt', 'w') as f:
    f.write(data)
