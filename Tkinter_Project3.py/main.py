from tkinter import *
from mypeople import MyPeople
from addpeople import AddPeople
from aboutus import AboutPeople
import datetime

date=datetime.datetime.now().date()
#print(str(date))
date=str(date)

class Application(object):
    def __init__(self,master):
        self.master=master
        #Frames
        self.top=Frame(master,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=500,bg='#34baba')
        self.bottom.pack(fill=X)

        '''Top Frame design'''
        self.top_image=PhotoImage(file='Icons/book.png.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=80,y=15)

        self.heading=Label(self.top,text='My PhoneBook App',font='arial 15 bold',
                            bg='white',fg='#ebb434')
        self.heading.place(x=230,y=70)

        self.date_lbl=Label(self.top,text="Today's Date:"+date,font='arial 15 bold',
                            fg='#ebb434',bg='white')
        self.date_lbl.place(x=400,y=110)

        '''Button-1:View People
           Button-2:Add People
           Button-3:About Us
        '''
        self.view_btn=Button(self.bottom,text='My People',fg='#42bcf5',bg='white',width=12,font='arial 12 bold',command=self.my_people)
        self.view_btn.place(x=250,y=70)

        self.add_btn=Button(self.bottom,text='Add People',fg='#42bcf5',bg='white',width=12,font='arial 12 bold',command=self.addpeople)
        self.add_btn.place(x=250,y=130)

        self.about_btn=Button(self.bottom,text='About People',fg='#42bcf5',bg='white',width=12,font='arial 12 bold',command=self.about_us)
        self.about_btn.place(x=250,y=190)
    

    '''Call My People File'''
    def my_people(self):
        people=MyPeople()

    def addpeople(self):
        add=AddPeople()

    def about_us(self):
        about_page=AboutPeople()





def main():
    root=Tk()
    app=Application(root)
    root.title("PhoneBook App")
    root.geometry('650x550+350+200')
    root.resizable(False,False)
    root.mainloop()

if __name__=="__main__":
    main()