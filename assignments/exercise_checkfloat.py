def getfloat():
    check = input("실수를 입력하시오")
    while not (check.isdigit() or isfloat(check)):
        check = input("실수를 입력하시오")
    return check

def isfloat(wtf):
    (a,_,b) = wtf.partition(".")
    return a.isdigit() and b.isdigit() or\
           (a[0]=="+"or a[0]=="-") and a[1:].isdigit() and\
           (b == "" or b.isdigit())

def check_float():
    ans = float(getfloat())
    print(ans)

check_float()
