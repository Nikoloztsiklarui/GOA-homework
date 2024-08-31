
def cal1():
    try:
        num1= float(input("please enter any number: "))
        num2= float(input("please enter any number: "))
    except ValueError:
        print("please enter valid number")
        return
    operation= input("enter type of operations(addition, subbtracion, multiplication, division ").strip().lower()
    if operation == "addition":
        print(num1 + num2)
    elif operation == "subbtracion":
        print(num1 - num2)
    elif operation == "multiplication":
        print(num1 * num2)
    elif operation == "division":
        if num2 == 0:
            print("please note that division by zero is impossebule")
        else:
            print(num1 / num2)
    else:
            print("please enter the correct type of opperation: addition, substracion, multiplication or division ")
cal1()


