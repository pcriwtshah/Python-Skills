'''
Vectors have magnitude and a direction. In 2D coordinate plane, 
vectors are represented by two numbers. In 3D coordinate place, 
it requires 3 numbers. Similarly, in n- dimensinal space, it 
requires n numbers. 
Vectors are added (or substracted) elementwise to form a new vectors.
Vectors are multiplied by a scalar( simply a number) to form a new vector.
We can use numpy package to work with vectors but for now we will create 
our own functions to work with vectors.
'''
''' Create a 3-dimensional vectors'''
name = ['Tom', 'Dick', 'Harry']
height = [65, 70, 63] #inches
weight = [160, 175, 180] #lbs
age = [35, 40, 45] #years

for i in range(3):
    print(f'{name[i]} is {age[i]} years old, {height[i]} inches tall and weigh {weight[i]} lbs')

vector = [name, height, weight, age]
print(vector)

#To add two vectors
def vector_add(v , w):
    '''Defining a function to add two vectors; requires two vectora as arguments'''
    x = []
    for i in range(len(v)):
        x.append(v[i] + w[i])
        i = i + 1
    return x
exam_1 = [75, 78, 89, 90, 95, 90]
exam_2 = [85, 86, 85, 93, 98, 100]
Total_Score = vector_add(exam_1, exam_2)
print(Total_Score)

def vector_subtract(v , w):
    '''Defining a function to subtract two vectors; requires two vectora as arguments'''
    x = []
    for i in range(len(v)):
        x.append(v[i] - w[i])
        i = i + 1
    return x

print(vector_subtract(exam_1, exam_2))