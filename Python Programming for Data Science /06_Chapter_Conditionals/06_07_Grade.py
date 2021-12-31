marks = int(input("Enter yur marks\n"))
if (marks >= 90):
    grade = "A"
#elif (marks >= 80 and marks <90):
elif(marks>=80):
    grade = "B"
elif(marks >=70):
    grade = "C"
elif(marks>=60):
    grade = "D"
else:
    grade = "F"
print(grade)
