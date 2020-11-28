def print_hi(name):
    print(f'BYE, {name}')

print("Hi, Welcome to the world of calculations !!")
cal_type = input("If you want to do BASIC calculations please type \' BASIC\' \nIf you want to do advanced calculations please type \'ADVANCED\' \n")
if cal_type == 'basic':
    import Basic
elif cal_type == 'advanced':
    import advncd
else:
    print(" THANK YOU")


if __name__ == '__main__':
    print_hi('THANK YOU')

