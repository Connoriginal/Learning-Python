from tkinter import *
from tkinter import messagebox
from BJgamestart import *
from BJcard import *
from BJlogin import *






class BlackJack(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=30, pady=20)
        self.menu()


    def menu(self):
        #self.GOD = PhotoImage(file = "jjangu.gif")
        #Label(self, image=self.GOD).grid(row=0)
        Label(self, text="\n\n").grid(row=0,column=4)
        Label(self, text="type :").grid(row=0,column=0)
        self.logtype = Text(self,width = 5,height =1 ,wrap = WORD)
        self.logtype.grid(row=0,column=1,sticky=W)
        Label(self, text="coin :").grid(row=0,column=2,sticky=W)
        self.coin = Text(self,width = 5,height =1, wrap = WORD)
        self.coin.grid(row=0,column=3,sticky=W)
        Label(self, text="\n\n\n").grid(row=1)
        Label(self, text="Black Jack",font = ("Helvetica 16 bold italic",44),relief="ridge").grid(row=1,column=4)
        Label(self, text="\n").grid(row=2)
        self.getname = Entry(self,width =10)
        self.getname.grid(row=3,column=5)
        Button(self, text ="login", command = self.get_player_info).grid(row=3,column=6)
        Label(self, text="\n\n\n\n").grid(row=4)
        Button(self, text="GameStart", command=self.jump_to_gamestart,cursor="spider").grid(row=5,column=4)
        Label(self, text=" ").grid(row=6,column=4)
        Button(self, text="My Page", command=self.jump_to_MP ,cursor="spider").grid(row=7,column=4)
        Label(self, text=" ").grid(row=8)
        name = self.getname.get()
        members = BringLogin.load_members()
        Button(self, text="Explain", command=self.jump_to_explain,cursor="spider").grid(row=9,column=4)
        Label(self, text=" ").grid(row=10)
        Button(self, text="Quit", command=self.quit,cursor="spider").grid(row=11,column=4)




    def jump_to_gamestart(self):
        self.name = self.getname.get()
        if self.name != "":
            GS = Tk()
            GS.title("Game Start")
            GS.geometry("400x150")
            GameStart(GS,self.name,self.leftmoney,self.win,self.playtime,self.members)
            GS.mainloop()
        else:
            NN = Tk()
            NN.title("!")
            NN.geometry("100x55")
            NN.configure(background="red")
            NN.option_add("*background", "red")
            Label(NN, text="Please Login!").pack()
            Button(NN, text ="Ok", command =NN.destroy).pack()
            NN.mainloop()

    def countdown(n):
        if n>0:
            time.sleep(1)
            countdown(n-1)


    def jump_to_MP(self):
        if self.name != "":
            MP = Tk()
            MP.title("My Page")
            MP.geometry("230x150")
            MP.name = self.getname.get()
            MP.members = BringLogin.load_members()
            Label(MP, text = MP.name).grid(row=0,column=0,sticky = E)
            Label(MP, text = "의 페이지").grid(row=0,column=1,sticky = W)
            Label(MP, text = "장착 뒷면 : ").grid(row=1,column=0,sticky = E)
            Label(MP, text = "승 수 : ").grid(row=2,column=0,sticky = E)
            Label(MP, text = MP.members[MP.name][1]+"회").grid(row=2,column=1,sticky = W)
            Label(MP, text = "승률 : ").grid(row=3,column=0,sticky = E)
            if int(MP.members[MP.name][2]) !=0 :
                Label(MP, text = str(round((int(MP.members[MP.name][1])/int(MP.members[MP.name][2]))*100,2))+"%").grid(row=3,column=1,sticky = W)
            else:
                Label(MP,text = "none").grid(row=3,column=1,sticky=W)
            Label(MP, text = "보유 코인 : ").grid(row=4,column=0,sticky = E)
            Label(MP, text =  MP.members[MP.name][0]+"개").grid(row=4,column=1,sticky = W)
            Button(MP, text = "회원 탈퇴", command = quit).grid(row=0,column=2)
            Button(MP, text ="그만볼래요", command = MP.destroy).grid(row=6,column=1)
            MP.mainloop()
        else:
            NN = Tk()
            NN.title("!")
            NN.geometry("100x55")
            NN.configure(background="red")
            NN.option_add("*background", "red")
            Label(NN, text="Please Login!").pack()
            Button(NN, text ="Ok", command =NN.destroy).pack()
            NN.mainloop()


    def get_player_info(self):
        name = self.getname.get()
        self.members = BringLogin.load_members()
        if name == "":
            self.name = 0
            self.leftmoney = 0
            self.win = 0
            self.playtime = 0
            logtype =  "none" #self.win  승수
            coin = self.leftmoney

        elif name in self.members.keys():
            self.name = name
            self.leftmoney = self.members[name][0]
            self.win = self.members[name][1]
            self.playtime = self.members[name][2]
            logtype =  "Old" #self.win  승수
            coin = self.leftmoney
        else:
            self.name = name
            self.leftmoney = int(1000)
            self.win = 0
            self.playtime = 0
            logtype = "New"
            coin = 1000
            self.members[name] = (self.leftmoney, self.win, self.playtime)
            BringLogin.store_members(self.members)
        self.logtype.delete(0.0,END)
        self.logtype.insert(0.0, logtype)
        self.coin.delete(0.0,END)
        self.coin.insert(0.0, coin)

    def jump_to_explain(self):
        explain = Tk()
        explain.title("Explain")
        explain.geometry("500x320")
        explain.configure(background="White")
        explain.option_add("*background", "White")
        #scroll= Scrollbar(explain)
        #scroll.pack(side=RIGHT, fill=Y)

        explain_text = Text(explain,width = 75,height =18)
        explain_text.insert(INSERT, "-----------------------------Black Jack이란?---------------------------\n")
        explain_text.insert(INSERT, "   프랑스에서 태어나 미국으로 넘어가 흥행을 일으키며 현재 카지노 1순위의 도박 게임입니다.\n\n")
        explain_text.insert(INSERT, "      이론적 승률 49.72%, 모든 카드 게임중에서 승률이 5:5에 가장 가까운 게임이며\n\n")
        explain_text.insert(INSERT, "     카지노 시설안에 있는 게임중에서 가장 실력으로 결과가 결정된다고 알려져 있습니다.\n")
        explain_text.insert(INSERT, "---------------------------------기본 룰--------------------------------\n")
        explain_text.insert(INSERT, "    딜러와 플레이어가 카드를 한장씩 주고받아 21에 가까운 사람이 이기는 게임입니다.\n\n")
        explain_text.insert(INSERT, "     카드 두장을 기본적으로 받게되며, 두장에 21이 나오면 BLACK JACK이 됩니다.\n\n")
        explain_text.insert(INSERT, "  21이 될 때 까지는 계속해서 카드를 받을 수 있지만 21이 넘어가면 배팅한 금액을 잃게됩니다.\n\n")
        explain_text.insert(INSERT, "         시작할 때 딜러는 한장을, 플레이어는 두장을 오픈한 채로 게임을 시작합니다.\n\n")
        explain_text.insert(INSERT, "                 J, Q, K는 숫자 10을 의미하며 상위관계가 없습니다.\n\n")
        explain_text.insert(INSERT, "              A는 1 또는 11 자신이 유리한 방향으로 지정할 수 있습니다.\n\n")
        explain_text.insert(INSERT, "------------------------------게임 용어 설명-----------------------------\n\n")
        explain_text.insert(INSERT, "                                < HIT >\n\n")
        explain_text.insert(INSERT, "     기본적으로 받게 되는 두장의 카드 이외에 카드를 더 뽑는 것을 HIT라고 합니다.\n")
        explain_text.insert(INSERT, "        히트로 인해 21이 되었을 경우 BLACK JACK이 아니며 숫자 21을 의미합니다.\n\n")
        explain_text.insert(INSERT, "                               < STAY >\n\n")
        explain_text.insert(INSERT, "            카드를 뽑지 않고 자신의 턴을 종료하는 것을 STAY라고 합니다.\n\n")
        explain_text.insert(INSERT, "                               < PUSH >\n\n")
        explain_text.insert(INSERT, "           딜러와 플레이어의 숫자가 같아 비기게 되는 경우를 PUSH라고 합니다.\n\n")
        explain_text.insert(INSERT, "                               < BURST >\n\n")
        explain_text.insert(INSERT, "            카드의 총 합이 21이 넘어 패배하는 것을 BURST라고 합니다.\n\n")
        explain_text.insert(INSERT, "                              < BLACKJACK >\n\n")
        explain_text.insert(INSERT, "          1인 A와 10, J, Q, K중 한장으로 이루어져 2장으로 합이 21일 경우\n\n")
        explain_text.insert(INSERT, "          BLACKJACK이라고 합니다.3장일 때 합이 21인 것보다 상위 개념입니다.\n\n")
        explain_text.insert(INSERT, "                              < EVEN MONEY >\n\n")
        explain_text.insert(INSERT, "         딜러가 오픈한 1장의 카드가 A이고, 플레이어가 BLACK JACK이 나왔을때 \n\n")
        explain_text.insert(INSERT, "       딜러가 자신의 2번째 장을 보지 않고 원래 BLACK JACK의 보상인 1.5배가 아닌 \n\n")
        explain_text.insert(INSERT, "               1배만 플레이어에게 지불하는 것을 EVEN MONEY라고 합니다.\n\n")
        explain_text.insert(INSERT, "                              < DOUBLE DOWN >\n\n")
        explain_text.insert(INSERT, "     21이 되지않는 한 무제한으로 카드를 뽑을 수 있으나, 카드를 한 장만 뽑는다는 조건하에\n\n")
        explain_text.insert(END, "             금액을 두배로 배팅하는 것을 DOUBLE DOWN 이라고 합니다.\n\n")
        explain_text.pack()
        Button(explain, text ="그만볼래요", command =explain.destroy).pack()
        #explain_text.config(yscrollcommand=scroll.set)
        #scroll.config(command=explain_text.yview)
        explain.mainloop()





class BlackjackController:
    root = Tk()
    root.title("Black Jack")
    root.geometry("650x500")
    root.configure(background="white")
    root.option_add("*background", "white")
    root.cursor="spider"
    #load = Image.open('bg.png')
    #render = ImageTk.PhotoImage(load)
    #img = Label(self, image = render)
    #img.image = render
    #img.place(x=0,y=0,relwidth =1,relheight=1)
    ###filename = PhotoImage(file = "backg.gif")
    #bgl = Label(root, image=filename)
    #bgl.place(x=0, y=0, height=650, width=500)
    BlackJack(root)
    root.mainloop()







#시작하기
BlackjackController()
