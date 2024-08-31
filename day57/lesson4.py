def goa1():
    try: 
        number=int(input("enter a number: "))
        if number % 2 == 0:
            print("evean")
        else:

                print("odd")
    except ValueError:
        print("please enter valid number")
goa1()
