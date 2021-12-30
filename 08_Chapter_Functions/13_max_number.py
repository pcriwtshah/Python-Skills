#Find the maximum of 3 numbers

def maximum(n1, n2, n3):
    if (n1>n2):
        if (n1>n3):
            return n1
        else:
            return n3
    else:
        if (n2>n3):
            return n2
        else:
            return n3

print(maximum(23,15,7))