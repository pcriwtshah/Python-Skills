#Create the tuple using ()
t = (1, 2, 3, 4, 5)
print(t)

print(t[2])
#Cannot replace value as in lists. it will show error.  tuple are immutable
#t[2] = 12
#print(t)

a = () #Empty tuple
b = (1,) #single element tuple, needs comma at the end
c = (1, 2, 3, 4, 2, 4, 2, 6, 7, 2) #multi element tuple

#Methods in tuple
d = c.count(2)
print(d)
print(c.count(4))
print(c.index(2))