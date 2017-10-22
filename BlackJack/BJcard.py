import random
from tkinter import *

class Card:
    """defines Card class"""
    __suits = ("Diamond", "Heart", "Spade", "Clover")
    __ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, rank, face_up = True):
        if suit in Card.__suits and rank in Card.__ranks:
            self.suit = suit
            self.rank = rank
            self.face_up = face_up
            if self.rank == "J" or self.rank == "Q" or self.rank == "K":
                self.value = 10
            elif self.rank == "A":
                self.value = 11
            else:
                self.value = int(self.rank)

            if self.suit =="Spade" and self.rank =="A":
                self.image = PhotoImage(file = "Spade_Ace.gif")
            if self.suit =="Spade" and self.rank =="2":
                self.image = PhotoImage(file = "Spade_2.gif")
            if self.suit =="Spade" and self.rank =="3":
                self.image = PhotoImage(file = "Spade_3.gif")
            if self.suit =="Spade" and self.rank =="4":
                self.image = PhotoImage(file = "Spade_4.gif")
            if self.suit =="Spade" and self.rank =="5":
                self.image = PhotoImage(file = "Spade_5.gif")
            if self.suit =="Spade" and self.rank =="6":
                self.image = PhotoImage(file = "Spade_6.gif")
            if self.suit =="Spade" and self.rank =="7":
                self.image = PhotoImage(file = "Spade_7.gif")
            if self.suit =="Spade" and self.rank =="8":
                self.image = PhotoImage(file = "Spade_8.gif")
            if self.suit =="Spade" and self.rank =="9":
                self.image = PhotoImage(file = "Spade_9.gif")
            if self.suit =="Spade" and self.rank =="10":
                self.image = PhotoImage(file = "Spade_10.gif")
            if self.suit =="Spade" and self.rank =="J":
                self.image = PhotoImage(file = "Spade_Jack.gif")
            if self.suit =="Spade" and self.rank =="Q":
                self.image = PhotoImage(file = "Spade_Queen.gif")
            if self.suit =="Spade" and self.rank =="K":
                self.image = PhotoImage(file = "Spade_King.gif")

            if self.suit =="Heart" and self.rank =="A":
                self.image = PhotoImage(file = "Heart_Ace.gif")
            if self.suit =="Heart" and self.rank =="2":
                self.image = PhotoImage(file = "Heart_2.gif")
            if self.suit =="Heart" and self.rank =="3":
                self.image = PhotoImage(file = "Heart_3.gif")
            if self.suit =="Heart" and self.rank =="4":
                self.image = PhotoImage(file = "Heart_4.gif")
            if self.suit =="Heart" and self.rank =="5":
                self.image = PhotoImage(file = "Heart_5.gif")
            if self.suit =="Heart" and self.rank =="6":
                self.image = PhotoImage(file = "Heart_6.gif")
            if self.suit =="Heart" and self.rank =="7":
                self.image = PhotoImage(file = "Heart_7.gif")
            if self.suit =="Heart" and self.rank =="8":
                self.image = PhotoImage(file = "Heart_8.gif")
            if self.suit =="Heart" and self.rank =="9":
                self.image = PhotoImage(file = "Heart_9.gif")
            if self.suit =="Heart" and self.rank =="10":
                self.image = PhotoImage(file = "Heart_10.gif")
            if self.suit =="Heart" and self.rank =="J":
                self.image = PhotoImage(file = "Heart_Jack.gif")
            if self.suit =="Heart" and self.rank =="Q":
                self.image = PhotoImage(file = "Heart_Queen.gif")
            if self.suit =="Heart" and self.rank =="K":
                self.image = PhotoImage(file = "Heart_King.gif")

            if self.suit =="Clover" and self.rank =="A":
                self.image = PhotoImage(file = "Clover_Ace.gif")
            if self.suit =="Clover" and self.rank =="2":
                self.image = PhotoImage(file = "Clover_2.gif")
            if self.suit =="Clover" and self.rank =="3":
                self.image = PhotoImage(file = "Clover_3.gif")
            if self.suit =="Clover" and self.rank =="4":
                self.image = PhotoImage(file = "Clover_4.gif")
            if self.suit =="Clover" and self.rank =="5":
                self.image = PhotoImage(file = "Clover_5.gif")
            if self.suit =="Clover" and self.rank =="6":
                self.image = PhotoImage(file = "Clover_6.gif")
            if self.suit =="Clover" and self.rank =="7":
                self.image = PhotoImage(file = "Clover_7.gif")
            if self.suit =="Clover" and self.rank =="8":
                self.image = PhotoImage(file = "Clover_8.gif")
            if self.suit =="Clover" and self.rank =="9":
                self.image = PhotoImage(file = "Clover_9.gif")
            if self.suit =="Clover" and self.rank =="10":
                self.image = PhotoImage(file = "Clover_10.gif")
            if self.suit =="Clover" and self.rank =="J":
                self.image = PhotoImage(file = "Clover_Jack.gif")
            if self.suit =="Clover" and self.rank =="Q":
                self.image = PhotoImage(file = "Clover_Queen.gif")
            if self.suit =="Clover" and self.rank =="K":
                self.image = PhotoImage(file = "Clover_King.gif")

            if self.suit =="Diamond" and self.rank =="A":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="2":
                self.image = PhotoImage(file = "Diamond_2.gif")
            if self.suit =="Diamond" and self.rank =="3":
                self.image = PhotoImage(file = "Diamond_3.gif")
            if self.suit =="Diamond" and self.rank =="4":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="5":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="6":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="7":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="8":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="9":
                self.image = PhotoImage(file = "Diamond_Ace.gif")
            if self.suit =="Diamond" and self.rank =="10":
                self.image = PhotoImage(file = "Diamond_10.gif")
            if self.suit =="Diamond" and self.rank =="J":
                self.image = PhotoImage(file = "Diamond_Jack.gif")
            if self.suit =="Diamond" and self.rank =="Q":
                self.image = PhotoImage(file = "Diamond_Queen.gif")
            if self.suit =="Diamond" and self.rank =="K":
                self.image = PhotoImage(file = "Diamond_King.gif")
            self.cardbackimage = PhotoImage(file = "facedown.gif")


    def flip(self):
        self.face_up = not self.face_up

    @staticmethod
    def fresh_deck():
        cards = []
        for s in Card.__suits:
            for r in Card.__ranks:
                cards.append(Card(s,r,False))
        random.shuffle(cards)
        return cards

class Deck:
    def __init__(self):
        self.deck = Card.fresh_deck()

    def next(self, open=True):
        if self.deck == []:
            self.deck = Card.fresh_deck()
        card = self.deck.pop()
        if open :
            card.flip()
        return card
