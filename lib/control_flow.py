#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
    if((username == 'admin' or username == 'ADMIN') and password == '12345'):
        return "Access granted"
    else:
        return "Access denied"
inn = admin_login("admin","12345")
print(inn)            


def hows_the_weather(temperature):
    # your code here
    pass
    if (temperature < 40) :
        response = "brisk"
    elif (temperature >= 40 and temperature <= 65) :
        response = "a little chilly"
    elif (temperature > 85) :
        response = "too dang hot"
    else :
        response = "perfect"
    return ( f"It's {response} out there!")
temp = hows_the_weather (80)
print (temp)           


def fizzbuzz(num):
    # your code here
    pass
    if num % 3 == 0 and num % 5 == 0 :
        return "FizzBuzz"
    elif num % 3  == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else :
        return num        

def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == "+" :
        return num1 + num2
    elif operation == "-" :
        return num1 - num2
    elif operation == "*" :
        return num1 * num2
    elif operation == "/" :
        if num2 != 0:
            return num1 / num2
        else :
            print("Cannot divide by zero!")
    else :
        print("Invalid operation!")
cal = calculator("*" ,2,8) 
print(cal)                 