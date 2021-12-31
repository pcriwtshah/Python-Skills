'''letter = |<Name>|'''

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to inform about your application.
You are selected!
Have a great day.
Thanks and Regards,
Bill

Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter today's date\n")
letter = letter.replace("<|NAME|>", name) # replaces <|NAME|> by input name and update letter.
letter = letter.replace("<|DATE|>", date)
print(letter)