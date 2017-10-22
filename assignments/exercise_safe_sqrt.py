def getfloat(wtf):
    (a,_,b) = wtf.partition(".")
    return a.isdigit() and b.isdigit()

def get_result(wtf):
    wtf = float(wtf)
    ans = round(wtf**(1/2),4)
    return ans

def stop():
    cont = input("계속하시겠습니까? (y/n)")
    while not (cont =="y" or cont == "n"):
        cont = input("계속하시겠습니까? (y/n)")
    return cont == "n"

def safe_sqrt():
    print("제곱근을 구해드립니다.")
    print("0이상의 수를 입력하세요.")
    while True:
        num = input("수를 입력하세요.")
        while not(num.isdigit() or getfloat(num)):
            num = input("수를 입력하세요.")
        ans = get_result(num)
        print(num,"의 제곱근은",ans,"입니다.")
        if stop():
            break
    print("안녕히 가세요.")

safe_sqrt()
