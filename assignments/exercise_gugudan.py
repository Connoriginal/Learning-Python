def gugudan1():
    for i in range(2,10):
        for k in range(2,10):
            if k == 5:
                print(i,"x",k,"=",str(i*k).rjust(2),end = "\n")
            elif k == 9:
                print(i,"x",k,"=",str(i*k).rjust(2),end = "\n\n")
            else:
                print(i,"x",k,"=",str(i*k).rjust(2),end = " ")

def gugudan2():
    for i in range(2,10):
        for k in range(2,6):
            if k ==5:
                print(k,"x",i,"=",str(k*i).rjust(2),end="\n")
            else:
                print(k,"x",i,"=",str(k*i).rjust(2),end=" ")
    print("\n")
    for i in range(2,10):
        for k in range(6,10):
            if k == 9:
                print(k,"x",i,"=",str(k*i).rjust(2),end="\n")
            else:
                print(k,"x",i,"=",str(k*i).rjust(2),end=" ")
gugudan1()
gugudan2()
