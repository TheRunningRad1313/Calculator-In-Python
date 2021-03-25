# print("Calculator in Python and if you want to exit then write exit at whatever stage")

num1 = ""
num2 = ""
sign = ""
result = ""

while num1 != "exit" and num2 != "exit" and sign != "exit":
    num1 = input("Enter Number 1: ")
    if (num1 == "exit"):
        exit(0)
    try:
        int(num1)
    except Exception as exception:
        print("Please Input a Integer")
        num1 = input("Enter Number 1: ")

    num2 = input("Enter Number 2: ")
    if (num2 == "exit"):
        exit(0)
    try:
        int(num2)
    except Exception as exception:
        print("Please Input a Integer")
        num2 = input("Enter Number 2: ")

    sign = input("Please Enter the Sign: ")
    if (sign == "exit"):
        exit(0)

    if (sign == "+"):
        try:
            result = float(num1) + float(num2)
            print(result)
        except Exception as exception:
            print("not able to convert the answer as the input is not a integer")
    elif (sign == "-"):
        try:
            result = float(num1) - float(num2)
            print(result)
        except Exception as exception:
            print("not able to convert the answer as the input is not a integer")
    elif (sign == "*"):
        try:
            result = float(num1) * float(num2)
            print(result)
        except Exception as exception:
            print("not able to convert the answer as the input is not a integer")
    elif (sign == "/"):
        try:
            result = float(num1) / float(num2)
            print(result)
        except Exception as exception:
            print("not able to convert the answer as the input is not a integer")            
    else:
        print("not able to tell the answer as the sign is not valid")
        sign = input("Please Enter the Sign: ")

    
