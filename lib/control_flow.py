#!/usr/bin/env python3

# Question 1:
def admin_login(username, password):
    if (username == "admin" or "ADMIN" and password == 12345):
       return "Acess granted"
    else:
        return "Acess denied"
    
    pass

# Question 2:
def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's chilly out there!"
    elif temperature >85:
        return "It's too dang hot!"
    else:
        return "It's perect out there!"
    
    pass
# Question 3
# Question 4
def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":

    else:
        return ("Division by zero is not allowed." or "Invalid operation!")