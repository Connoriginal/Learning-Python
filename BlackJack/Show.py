from tkinter import *
class BlackJack(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=30, pady=20)
        self.create_widgets()
    def create_widgets(self):
        self.SA = PhotoImage(file = "Spade_Ace.gif")
        self.S2 = PhotoImage(file = "Spade_2.gif")
        self.S3 = PhotoImage(file = "Spade_3.gif")
        self.S4 = PhotoImage(file = "Spade_4.gif")
        self.S5 = PhotoImage(file = "Spade_5.gif")
        self.S6 = PhotoImage(file = "Spade_6.gif")
        self.S7 = PhotoImage(file = "Spade_7.gif")
        self.S8 = PhotoImage(file = "Spade_8.gif")
        self.S9 = PhotoImage(file = "Spade_9.gif")
        self.S0 = PhotoImage(file = "Spade_10.gif")
        self.SJ = PhotoImage(file = "Spade_Jack.gif")
        self.SQ = PhotoImage(file = "Spade_Queen.gif")
        self.SK = PhotoImage(file = "Spade_King.gif")
        self.HA = PhotoImage(file = "Heart_Ace.gif")
        self.H2 = PhotoImage(file = "Heart_2.gif")
        self.H3 = PhotoImage(file = "Heart_3.gif")
        self.H4 = PhotoImage(file = "Heart_4.gif")
        self.H5 = PhotoImage(file = "Heart_5.gif")
        self.H6 = PhotoImage(file = "Heart_6.gif")
        self.H7 = PhotoImage(file = "Heart_7.gif")
        self.H8 = PhotoImage(file = "Heart_8.gif")
        self.H9 = PhotoImage(file = "Heart_9.gif")
        self.H0 = PhotoImage(file = "Heart_10.gif")
        self.HJ = PhotoImage(file = "Heart_Jack.gif")
        self.HQ = PhotoImage(file = "Heart_Queen.gif")
        self.HK = PhotoImage(file = "Heart_King.gif")
        self.CA = PhotoImage(file = "Clover_Ace.gif")
        self.C2 = PhotoImage(file = "Clover_2.gif")
        self.C3 = PhotoImage(file = "Clover_3.gif")
        self.C4 = PhotoImage(file = "Clover_4.gif")
        self.C5 = PhotoImage(file = "Clover_5.gif")
        self.C6 = PhotoImage(file = "Clover_6.gif")
        self.C7 = PhotoImage(file = "Clover_7.gif")
        self.C8 = PhotoImage(file = "Clover_8.gif")
        self.C9 = PhotoImage(file = "Clover_9.gif")
        self.C0 = PhotoImage(file = "Clover_10.gif")
        self.CJ = PhotoImage(file = "Clover_Jack.gif")
        self.CQ = PhotoImage(file = "Clover_Queen.gif")
        self.CK = PhotoImage(file = "Clover_King.gif")
        self.DA = PhotoImage(file = "Diamond_Ace.gif")
        self.D2 = PhotoImage(file = "Diamond_2.gif")
        self.D3 = PhotoImage(file = "Diamond_3.gif")
        self.D4 = PhotoImage(file = "Diamond_4.gif")
        self.D5 = PhotoImage(file = "Diamond_5.gif")
        self.D6 = PhotoImage(file = "Diamond_6.gif")
        self.D7 = PhotoImage(file = "Diamond_7.gif")
        self.D8 = PhotoImage(file = "Diamond_8.gif")
        self.D9 = PhotoImage(file = "Diamond_9.gif")
        self.D0 = PhotoImage(file = "Diamond_10.gif")
        self.DJ = PhotoImage(file = "Diamond_Jack.gif")
        self.DQ = PhotoImage(file = "Diamond_Queen.gif")
        self.DK = PhotoImage(file = "Diamond_King.gif")

        Label(self, image=self.SA).grid(row=0,column=0)
        Label(self, image=self.S2).grid(row=0,column=1)
        Label(self, image=self.S3).grid(row=0,column=2)
        Label(self, image=self.S4).grid(row=0,column=3)
        Label(self, image=self.S5).grid(row=0,column=4)
        Label(self, image=self.S6).grid(row=0,column=5)
        Label(self, image=self.S7).grid(row=0,column=6)
        Label(self, image=self.S8).grid(row=0,column=7)
        Label(self, image=self.S9).grid(row=0,column=8)
        Label(self, image=self.S0).grid(row=0,column=9)
        Label(self, image=self.SJ).grid(row=0,column=10)
        Label(self, image=self.SQ).grid(row=0,column=11)
        Label(self, image=self.SK).grid(row=0,column=12)
        Label(self, image=self.HA).grid(row=1,column=0)
        Label(self, image=self.H2).grid(row=1,column=1)
        Label(self, image=self.H3).grid(row=1,column=2)
        Label(self, image=self.H4).grid(row=1,column=3)
        Label(self, image=self.H5).grid(row=1,column=4)
        Label(self, image=self.H6).grid(row=1,column=5)
        Label(self, image=self.H7).grid(row=1,column=6)
        Label(self, image=self.H8).grid(row=1,column=7)
        Label(self, image=self.H9).grid(row=1,column=8)
        Label(self, image=self.H0).grid(row=1,column=9)
        Label(self, image=self.HJ).grid(row=1,column=10)
        Label(self, image=self.HQ).grid(row=1,column=11)
        Label(self, image=self.HK).grid(row=1,column=12)
        Label(self, image=self.CA).grid(row=2,column=0)
        Label(self, image=self.C2).grid(row=2,column=1)
        Label(self, image=self.C3).grid(row=2,column=2)
        Label(self, image=self.C4).grid(row=2,column=3)
        Label(self, image=self.C5).grid(row=2,column=4)
        Label(self, image=self.C6).grid(row=2,column=5)
        Label(self, image=self.C7).grid(row=2,column=6)
        Label(self, image=self.C8).grid(row=2,column=7)
        Label(self, image=self.C9).grid(row=2,column=8)
        Label(self, image=self.C0).grid(row=2,column=9)
        Label(self, image=self.CJ).grid(row=2,column=10)
        Label(self, image=self.CQ).grid(row=2,column=11)
        Label(self, image=self.CK).grid(row=2,column=12)
        Label(self, image=self.DA).grid(row=3,column=0)
        Label(self, image=self.D2).grid(row=3,column=1)
        Label(self, image=self.D3).grid(row=3,column=2)
        Label(self, image=self.D4).grid(row=3,column=3)
        Label(self, image=self.D5).grid(row=3,column=4)
        Label(self, image=self.D6).grid(row=3,column=5)
        Label(self, image=self.D7).grid(row=3,column=6)
        Label(self, image=self.D8).grid(row=3,column=7)
        Label(self, image=self.D9).grid(row=3,column=8)
        Label(self, image=self.D0).grid(row=3,column=9)
        Label(self, image=self.DJ).grid(row=3,column=10)
        Label(self, image=self.DQ).grid(row=3,column=11)
        Label(self, image=self.DK).grid(row=3,column=12)



root = Tk()
root.title("Black_Jack")
root.geometry("1100x500")
root.configure(background="Yellow")
root.option_add("*background", "Yellow")
BlackJack(root)
root.mainloop()
