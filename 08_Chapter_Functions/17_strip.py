def remove_and_strip(string, word):
    new_string = string.replace(word, "")
    return new_string

sentence = "Weather is very good today"
print(sentence)
print(remove_and_strip(sentence, "Weather"))
