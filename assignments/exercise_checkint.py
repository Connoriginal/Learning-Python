def get_int():
    a = input("정수를 입력하시오")
    while not (a.isdigit() or\
               a[0]=="+" and a[1:].isdigit() or\
               a[0]=="-" and a[1:].isdigit()):
        a = input("정수를 입력하시오")
    return a

def  check_int():
    a = get_int()
    intc = int(a)
    print(intc)

check_int()
