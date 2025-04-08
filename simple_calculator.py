while True:
    num1=input("Enter a number:")
    num2=input("Enter a number:")
    operations=input("Enter a Operation (+,-,*,/,//,**,%):")
    try:
      num1=float(num1)
      num2=float(num2)
      if operations == "+":
        print(f"The addition of {num1} + {num2} is {num1 + num2}")
      elif operations == "-":
        print(f"The subtraction of {num1} - {num2} is {num1 - num2}")
      elif operations == "*":
        print(f"The multiplication of {num1} * {num2} is {num1 * num2}")
      elif operations == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"The division of {num1} / {num2} is {num1 / num2}")
      elif operations == "//":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"The floor division of {num1} // {num2} is {num1 // num2}")
      elif operations == "**":
            print(f"{num1} raised to {num2} is {num1 ** num2}")  # Fixed label
      elif operations == "%":
        if num2 == 0:
            print("Error: Cannot compute remainder with zero!")
        else:
            print(f"The remainder of {num1} % {num2} is {num1 % num2}")
      else:
        print("Incorrect operation. Please use +, -, *, /, //, **, or %.")
      retry =input("Try again? (yes/no):").lower()
      if retry == "no":
        print("Goodbye!")
        break
    except ValueError:
      print("Incorrect Input: Please enter valid numbers.")
