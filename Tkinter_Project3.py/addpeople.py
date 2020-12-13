from tkinter import *
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('650x650+600+200')
        self.title('Add New Person')
        #self.resizable(False,False)

        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg='#34baeb')
        self.bottom.pack(fill=X)

        '''Top Frame design'''
        self.top_image=PhotoImage(file='Icons/people.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=80,y=15)

        self.heading=Label(self.top,text='Add New Person',font='arial 15 bold',
                            bg='white',fg='#ebb134')
        self.heading.place(x=230,y=70)

        '''Name,Surname,Email,Address,Phone no.'''
        self.label_name=Label(self.bottom,text='Name',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_name.place(x=40,y=40)

        self.entry_name=Entry(self.bottom,width=30,bd=4)
        self.entry_name.insert(0,'Enter Name')
        self.entry_name.place(x=150,y=40)

        self.label_surname=Label(self.bottom,text='Surname',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_surname.place(x=40,y=80)

        self.entry_surname=Entry(self.bottom,width=30,bd=4)
        self.entry_surname.insert(0,'Enter SurName')
        self.entry_surname.place(x=150,y=80)

        self.label_phone=Label(self.bottom,text='Phone No',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_phone.place(x=40,y=120)

        self.entry_phone=Entry(self.bottom,width=30,bd=4)
        self.entry_phone.insert(0,'Enter Phone Number')
        self.entry_phone.place(x=150,y=120)

        self.label_email=Label(self.bottom,text='Email',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_email.place(x=40,y=160)

        self.entry_email=Entry(self.bottom,width=30,bd=4)
        self.entry_email.insert(0,'Enter Email here')
        self.entry_email.place(x=150,y=160)

        self.label_address=Label(self.bottom,text='Address',font='arial 15 bold',fg='white',bg='#fcc324')
        self.label_address.place(x=40,y=200)

        self.entry_address=Text(self.bottom,width=30,bd=4,height=12)
        self.entry_address.place(x=150,y=200)

        submit=Button(self.bottom,text='Add Person',command=self.add_people)
        submit.place(x=250,y=460)

    def add_people(self):
        name=self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone=self.entry_phone.get()
        address=self.entry_address.get(1.0,'end-1c')
        
        if name and surname and email and phone and address!="":
            try:
                #fill to the database
                query="insert into 'addressbook' (person_name,person_surname,person_email,person_phone,person_address) values(?,?,?,?,?)"
                cur.execute(query,(name,surname,email,phone,address))
                con.commit()
                messagebox.showinfo('Success','Contact Add')

            except Exception as e:
                messagebox.showerror('Error',str(e))
        else:
            messagebox.showerror('Error','fill all the fields',icon='warning')

