from tkinter import *
from BJcard import *
from BJlogin import *



class GameStart(Frame):
    def __init__(self,GS,name,leftmoney,win,playtime,members):
        super().__init__(GS)
        self.pack(padx= 30, pady = 20)
        self.name = name
        self.leftmoney = int(leftmoney)
        self.win = int(win)
        self.playtime = int(playtime)
        self.members = members
        self.get_bet()



    def get_bet(self):
        Label(self, text="How much will you bet? please bet 50 ~ 100 coin!",font=("nomal",15)).grid(row=0)
        self.choosebet = Entry(self,width =10)
        self.choosebet.grid(row=1)
        self.check_bet_money = Text(self, width= 40, height=1, wrap = WORD)
        self.check_bet_money.grid(row=3)
        Button(self, text = "GoGo!",command = self.go_to_checkbetmoney).grid(row=2)



    def go_to_checkbetmoney(self):
        self.betmoney= self.choosebet.get()
        if not self.betmoney.isdigit():
            ment = "it's not a number!"
            self.check_bet_money.delete(0.0,END)
            self.check_bet_money.insert(0.0,ment)
        elif not(50 <= int(self.betmoney) <= 100):
            ment = "your bet money is out of range!"
            self.check_bet_money.delete(0.0,END)
            self.check_bet_money.insert(0.0,ment)
        else:
            window = Toplevel()
            window.title("Casino")
            window.geometry("900x900")
            Play(window,self.name,self.leftmoney,self.win,self.playtime,self.betmoney,self.members)




class Play(Frame):
    def __init__(self,window,name,leftmoney,win,playtime,betmoney,members):
        super().__init__(window)
        self.window = window
        self.pack(padx = 30, pady =20)
        self.name = name
        self.leftmoney = int(leftmoney) - int(betmoney)
        self.win = int(win)
        self.playtime = playtime
        self.betmoney = betmoney
        self.ddeck = Deck()
        self.bettingmoney = int(self.betmoney)*2
        self.members = members
        self.play()



    def selectA(self,valuesum,a_num,alreadydid = True):
        if a_num == 0:
            return valuesum,alreadydid
        else:
            if alreadydid == True:
                return valuesum, alreadydid
            else:
                alreadydid = True
                return valuesum - 10, alreadydid


    def play(self):

        """페시브"""
        Label(self,text = "Playername: ").grid(row=0,column=0)
        Label(self,text = self.name).grid(row=0,column=1)
        Label(self,text = ", Leftmoney: ").grid(row=0,column=2)
        Label(self,text = self.leftmoney).grid(row=0,column=3)
        Label(self,text = ", Wins: ").grid(row=0,column=4)
        Label(self,text = self.win).grid(row=0,column=5)
        Label(self,text = ", playtime: ").grid(row=0,column=6)
        Label(self,text = self.playtime).grid(row=0,column=7)
        """시작"""

        """카드 지정"""
        self.dealer_card1 = self.ddeck.next(open)
        self.dealer_card2 = self.ddeck.next()
        self.player_card1 = self.ddeck.next(open)
        self.player_card2 = self.ddeck.next(open)
        """딜러 카드 보여주기 레이블"""
        Label(self,text = "Dealer").grid(row=1,column=0)
        Label(self, image = self.dealer_card1.image).grid(row=1,column=1)
        Label(self, image = self.dealer_card1.cardbackimage).grid(row=1,column = 2)
        """배팅머니 보여주기 텍스트"""
        Label(self,text = "Bettingmoney",font = ("normal",30)).grid(row=2,column=0)
        self.bettingmoney_pos = Text(self,width = 6, height = 1, wrap =WORD,font = ("normal",30))
        self.bettingmoney_pos.grid(row = 2,column=1)
        self.bettingmoney_pos.delete(0.0,END)
        bettingmoney = str(self.bettingmoney)
        self.bettingmoney_pos.insert(0.0,bettingmoney)
        """승리,패배 보여주기텍스트"""
        self.result = Text(self,width = 10, height = 1,font = ("normal",30), wrap = WORD)
        self.result.grid(row=5,column=1)
        self.result.delete(0.0,END)
        """손님 카드 보여주기 레이블"""
        Label(self,text = "Player").grid(row=3,column = 0)
        Label(self, image = self.player_card1.image).grid(row=3,column=1)
        Label(self, image = self.player_card2.image).grid(row=3, column=2)

        """변수"""
        self.dealersum = self.dealer_card1.value + self.dealer_card2.value
        self.dealer_A_num = 0
        self.alreadydid_d = False
        if self.dealer_card1.rank=="A" or self.dealer_card2=="A":
            self.dealer_A_num += 1
        if self.dealersum > 21 and self.dealer_A_num != 0:
            self.dealersum -= 10
            self.alreadydid_d = True

        self.playersum = self.player_card1.value + self.player_card2.value
        self.player_A_num = 0
        """A 1 or 11 구별"""
        self.alreadydid_p = False
        if self.player_card1.rank == "A" or self.player_card2.rank == "A":
            self.player_A_num += 1
        if self.playersum > 21 and self.player_A_num != 0:
            self.playersum -= 10
            self.alreadydid_p = True


        self.dealercolumn = 2
        self.playercolumn = 2
        self.pluscardnum = 0
        self.plusdealer_cardnum = 0

        Button(self, text = "Hit", command = self.jump_to_hit).grid(row=4,column=0)
        Button(self, text = "Stay", command = self.jump_to_stay).grid(row=4, column=1)
        self.Doubledoun =Button(self)
        self.Doubledoun["text"]="Doubledoun"
        self.Doubledoun["command"] = self.jump_to_doubledown
        self.Doubledoun.grid(row=4,column=2)



        """시작 row=4 부터 시작"""
        """블랙잭 판별"""
        if self.playersum == 21:
            self.result.insert(0.0,"BlackJack!")
            if self.dealer_card1.rank == "A":
                Label(self,text = " but Even money!").grid(row=2,column=3)
                self.leftmoney += self.bettingmoney
            else:
                self.leftmoney += self.bettingmoney * 2
            self.win += 1
            self.playtime += 1
            Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
            self.members[self.name] = (self.leftmoney, self.win, self.playtime)
            BringLogin.store_members(self.members)
            Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
            Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
            Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
            Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)

    def jump_to_hit(self):
        self.Doubledoun.grid_forget()
        self.card = self.ddeck.next(open)
        if self.card.rank == "A":
            self.player_A_num += 1
        self.playercolumn += 1
        if self.pluscardnum == 0:
            self.cardp0 = self.card
            Label(self,image = self.cardp0.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 1:
            self.cardp1 = self.card
            Label(self,image = self.cardp1.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 2:
            self.cardp2 = self.card
            Label(self,image = self.cardp2.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 3:
            self.cardp3 = self.card
            Label(self,image = self.cardp3.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 4:
            self.cardp4 = self.card
            Label(self,image = self.cardp4.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 5:
            self.cardp5 = self.card
            Label(self,image = self.cardp5.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 6:
            self.cardp6 = self.card
            Label(self,image = self.cardp6.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 7:
            self.cardp7 = self.card
            Label(self,image = self.cardp7.image).grid(row=3,column = self.playercolumn)
        elif self.pluscardnum == 8:
            self.cardp8 = self.card
            Label(self,image = self.cardp8.image).grid(row=3,column = self.playercolumn)
        self.pluscardnum += 1
        self.playersum += int(self.card.value)
        Button(self, text = "Hit", command = self.jump_to_hit).grid(row=4,column=0)
        Button(self, text = "Stay", command = self.jump_to_stay).grid(row=4, column=1)
        self.playersum, self.alreadydid_p = self.selectA(self.playersum,self.player_A_num,self.alreadydid_p)
        if self.playersum > 21:
            self.result.insert(0.0,"Burst!!")
            self.playtime += 1
            Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
            self.members[self.name] = (self.leftmoney, self.win, self.playtime)
            BringLogin.store_members(self.members)
            Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
            Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
            Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
            Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)

    def jump_to_stay(self):
        self.Doubledoun.grid_forget()
        if self.playersum > 21:
            self.result.insert(0.0,"Burst!!")
            self.playtime += 1
            Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
            self.members[self.name] = (self.leftmoney, self.win, self.playtime)
            BringLogin.store_members(self.members)
            Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
            Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
            Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
            Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
        else:
            while self.dealersum <= 16:
                self.card = self.ddeck.next(open)
                self.dealercolumn += 1
                if self.plusdealer_cardnum == 0:
                    self.cardd0 = self.card
                    Label(self,image = self.cardd0.image).grid(row=1,column=self.dealercolumn)
                elif self.plusdealer_cardnum== 1:
                    self.cardd1 = self.card
                    Label(self,image = self.cardd1.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 2:
                    self.cardd2 = self.card
                    Label(self,image = self.cardd2.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 3:
                    self.cardd3 = self.card
                    Label(self,image = self.cardd3.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 4:
                    self.cardd4 = self.card
                    Label(self,image = self.cardd4.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 5:
                    self.cardd5 = self.card
                    Label(self,image = self.cardd5.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 6:
                    self.cardd6 = self.card
                    Label(self,image = self.cardd6.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 7:
                    self.cardd7 = self.card
                    Label(self,image = self.cardd7.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 8:
                    self.cardd8 = self.card
                    Label(self,image = self.cardd1.image).grid(row=1,column = self.dealercolumn)
                self.plusdealer_cardnum +=1
                self.dealersum += int(self.card.value)
                if self.card.rank == "A":
                    self.dealer_A_num += 1
                self.dealer,alreadydid_d = self.selectA(self.dealersum,self.dealer_A_num,self.alreadydid_d)
            if self.dealersum > 21:
                self.result.insert(0.0,"Dealer Burst! You Win!")
                self.leftmoney += self.bettingmoney
                self.win += 1
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
            elif self.dealersum == self.playersum:
                self.result.insert(0.0,"Push!")
                self.leftmoney += int(self.betmoney)
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
            elif self.dealersum < self.playersum:
                self.result.insert(0.0,"You Win!")
                self.leftmoney += self.bettingmoney
                self.win += 1
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
            else:
                self.result.insert(0.0,"You Lose!")
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)

    def jump_to_doubledown(self):
        self.card = self.ddeck.next(open)
        self.playercolumn += 1
        Label(self, image = self.card.image).grid(row=3, column = self.playercolumn)
        self.leftmoney -= int(self.betmoney)
        self.bettingmoney += int(self.betmoney) * 2
        self.bettingmoney_pos.delete(0.0,END)
        bettingmoney = str(self.bettingmoney)
        self.bettingmoney_pos.insert(0.0,bettingmoney)
        self.playersum += int(self.card.value)
        if self.playersum > 21 and self.player_A_num != 0:
            self.playersum -= 10
        if self.playersum > 21:
            self.result.insert(0.0, "Burst!")
            self.playtime += 1
            Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
            self.mambers[self.name] = (self.leftmoney, self.win, self.playtime)
            BringLogin.store_members(self.members)
            Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
            Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
            Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
            Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
        else:
            while self.dealersum <= 16:
                self.card = self.ddeck.next(open)
                self.dealercolumn += 1
                if self.plusdealer_cardnum == 0:
                    self.cardd0 = self.card
                    Label(self,image = self.cardd0.image).grid(row=1,column=self.dealercolumn)
                elif self.plusdealer_cardnum== 1:
                    self.cardd1 = self.card
                    Label(self,image = self.cardd1.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 2:
                    self.cardd2 = self.card
                    Label(self,image = self.cardd2.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 3:
                    self.cardd3 = self.card
                    Label(self,image = self.cardd3.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 4:
                    self.cardd4 = self.card
                    Label(self,image = self.cardd4.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 5:
                    self.cardd5 = self.card
                    Label(self,image = self.cardd5.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 6:
                    self.cardd6 = self.card
                    Label(self,image = self.cardd6.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 7:
                    self.cardd7 = self.card
                    Label(self,image = self.cardd7.image).grid(row=1,column = self.dealercolumn)
                elif self.plusdealer_cardnum== 8:
                    self.cardd8 = self.card
                    Label(self,image = self.cardd1.image).grid(row=1,column = self.dealercolumn)
                self.plusdealer_cardnum +=1
                self.dealersum += int(self.card.value)
                if self.card.rank == "A":
                    self.dealer_A_num += 1
                self.dealer,alreadydid_d = selectA(self.dealersum,self.dealer_A_num,self.alreadydid_d)
            if self.dealersum > 21:
                self.result.insert(0.0,"Dealer Busrt!")
                self.leftmoney += self.bettingmoney
                self.win += 1
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.mambers[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
            elif self.dealersum == self.playersum:
                self.result.insert(0.0,"Draw")
                self.leftmoney += int(self.betmoney)
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
            elif self.dealersum < self.playersum:
                self.result.insert(0.0,"You Win!")
                self.leftmoney += self.bettingmoney
                self.win += 1
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)
            elif self.dealersum > self.playersum:
                self.result.insert(0.0,"You Lose!")
                self.playtime += 1
                Label(self, image = self.dealer_card2.image).grid(row=1,column = 2)
                self.members[self.name] = (self.leftmoney, self.win, self.playtime)
                BringLogin.store_members(self.members)
                Button(self,text = "Go to new game",command =self.jump_to_newgame).grid(row=4,column=0)
                Button(self,text="Close",command=self.window.destroy).grid(row=4,column=1)
                Label(self,text="Money: "+str(self.leftmoney)+",win: "+str(self.win) +"Playtime: "+str(self.playtime),font = ("normal",20)).grid(row=6,column=1)
                Label(self,text ="Please press the 'Close' button after you press 'Go to new game'",font=("normal",15)).grid(row=7,column=1)

    def jump_to_newgame(self):
        GS = Tk()
        GS.title("Game Start")
        GS.geometry("400x150")
        GameStart(GS,self.name,self.leftmoney,self.win,self.playtime,self.members)
        GS.mainloop()
