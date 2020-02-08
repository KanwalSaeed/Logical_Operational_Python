# and Logical AND "if both the operands are true then condition become true" (a and b) is true

# "lOGIN CREDENTIAL"
user_name = input("Enter User Nmae: ")
pass_word = input("Enter password: ")
if user_name == "Admin" and pass_word == "Admin":
    print("Login sucessfully")
else:
    print("You have entered wrong User Name or Password")





# or Logical OR "if any two of operand are non zero then condition become true" (a or b) is true

degree = input("Enter your BS Degree: ")
if degree == "cs" or "CSE":
    print("You are eligible.")
else:
    print("Yu are n't eligible.")



percentage = int(input("Enter your percentage: "))
city = input("Enter your city: ")
if percentage > 70 and city == "Karachi" or city == "Lahore":
    print("Congrates, you are selected for Job.")
else:
    print("Sorry, You are n't selected.")





# not Logical NOT "used to reverse the logical state of its operand" NOT (a and b ) is false

is_valid = True
city = input("Enter your city name: ")
if city == "Lahore":
    is_valid = False
if not is_valid:
    print("You are not eligible to apply here")
else:
    print("You are eligible and yoou can apply. ")