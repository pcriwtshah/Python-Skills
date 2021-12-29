#Decide if a student pass or fail
eng_marks = float(input("Enter the marks for Englsih"))
math_marks = float(input("Enter the marks for Math"))
science_marks = float(input("Enter the marks for Sciene"))
social_study_marks = float(input("Enter the marks for Social Study"))

if eng_marks >=60 and math_marks >=60 and science_marks >=60 and social_study_marks >=60:
    print("Congrats! You pass the exam")
else:
    print("Sorry! Best of luck next time")

#To find which subject a student fail
#marks = [eng_marks, math_marks, science_marks, social_study_marks]
