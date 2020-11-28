def adv_cal():
    print("1. Reciprocal or Multiplicative inverse of a number ")
    print("2. square root of a number")
    print("3. cube root of a number")
    print("4. factorial of a number")
    print("5. x^y")
    print("6. Power of ten (10^x)")
    print("7. square of a number")
    opt = int(input("Choose the Number specified before each operation to be performed:"))
    if opt == 1:
        return reciprocal()
    elif opt == 2:
        return sqrt()
    elif opt == 3:
        return cubert()
    elif opt == 4:
        return factorial()
    elif opt == 5:
        return xy()
    elif opt == 6:
        return ten()
    elif opt == 7:
        return sqr()
    else:
        print("INVALID")


def reciprocal():
    rec = float(input("Enter the number to find the reciprocal: "))
    res = 1/rec
    return res


def sqrt():
    rec = float(input("Enter the number to find the square root: "))
    res = pow(rec, 0.5)
    return res


def cubert():
    rec = float(input("Enter the number to find the cube root: "))
    res = pow(rec, 1/3)
    return round(res)


def factorial():
    rec = int(input("Enter the number to find the factorial: "))
    res = 1
    for i in range(1, rec+1):
        res *= i
    return res


def xy():
    rec = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    res = pow(rec, y)
    return res


def ten():
    rec = float(input("Enter the number: "))
    res = pow(10, rec)
    return res


def sqr():
    rec = float(input("Enter the number to find the square: "))
    res = rec * rec
    return res


rept = 'y'
while rept == 'y':
    adv_res = adv_cal()
    print("The result is", adv_res)
    rept = input("If you want to do more calculations, type \'y\' else press ENTER KEY")
