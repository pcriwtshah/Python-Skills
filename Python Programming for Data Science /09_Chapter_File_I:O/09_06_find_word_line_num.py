#Find a word in a file and a line number

content = True
i = 1
with open('09_01_poem.txt') as f:
    while content:
        content = f.readline()
        if 'twinkle' in content.lower():
            print(content)
            print(f"Yes, Twinkle is present in line number {i}")
        i += 1