
def oprtn(a, b):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Division")
    print("4.Multiplication")
    #print("5.Percentage")
    print("5.Remainder")
    print("Choose the Number specified before each operation to be performed:")
    oper_selectd = input(" ")
    if oper_selectd == "1":
        return add(a, b)
    elif oper_selectd == "2":
        return sub(a, b)
    elif oper_selectd == "3":
        return div(a, b)
    elif oper_selectd == "4":
        return mul(a, b)
    elif oper_selectd == "5":
        return rem(a, b)
    else:
        print("INVALID")


def add(num1, num2):
    num3 = num1 + num2
    return num3


def sub(num1, num2):
    num3 = num1-num2
    return num3


def div(num1, num2):
    num3 = num1/num2
    return num3


def mul(num1, num2):
    num3 = num1*num2
    return num3


def rem(num1, num2):
    num3 = num1 % num2
    return num3

#def adv():


rept = 'y'
while rept == 'y':
    num1 = int(input("Enter the number1: "))
    num2 = int(input("Enter the number2: "))
    res = oprtn(num1, num2)
    print("The result is ", res)
    rept = input("If you want to do more calculations, type \'y\' else press ENTER KEY")
else:
    #adv()
    #print()
    cal_type = input("\nIf you want to do advanced calculations please type \'ADVANCED\' \n else press enter")
    if cal_type == "advanced":
        import advncd
    else:
        #print("To exit from the calculator, please press ENTER KEY")
        quit()



    









































