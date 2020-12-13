from tkinter import *
from tkinter import messagebox
import sqlite3




class AboutPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('550x550+550+200')
        self.title('About Person')

        
        self.top=Frame(self,height=550,width=550,bg='#ffa500')
        self.top.pack(fill=BOTH)

        self.text=Label(self.top,text='Hey this is about us page'
                        '\n this application is made for educational Purpose'
                        '\n you can contact us on'
                        '\nFacebook'
                        '\nInstagram',
                        font='arial 15 bold',bg='#ffa500',fg='white')
        self.text.place(x=50,y=50)
      