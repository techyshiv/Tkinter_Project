from tkinter import *
from tkinter import messagebox
from addpeople import AddPeople
from updatepeople import UpdatePeople
from display import DisplayPeople
import sqlite3

con=sqlite3.connect('database.db')
cur=con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('650x650+600+200')
        self.title('My People')
        self.resizable(False,False)

        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=500,bg='#ebb134')
        self.bottom.pack(fill=X)

        '''Top Frame design'''
        self.top_image=PhotoImage(file='Icons/people.png')
        self.top_image_label=Label(self.top,image=self.top_image,bg='white')
        self.top_image_label.place(x=80,y=15)

        self.heading=Label(self.top,text='My People',font='arial 15 bold',
                            bg='white',fg='#34baeb')
        self.heading.place(x=230,y=70)

        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)
        

        self.listbox=Listbox(self.bottom,width=40,height=27)
        self.listbox.grid(row=0,column=0,padx=(40,0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        persons=cur.execute("select * from 'addressbook'").fetchall()
        count=0
        for person in persons:
            self.listbox.insert(count,str(person[0])+ " " + person[1] +" " + person[2])
            count+=1
        

        self.scroll.grid(row=0,column=1,sticky=N+S)

        '''Buttons'''
        btn_add=Button(self.bottom,text='ADD',width=12,font='Sans 12 bold',command=self.add_people)
        btn_add.grid(row=0,column=2,padx=20,pady=10,sticky=N)

        btn_update=Button(self.bottom,text='UPDATE',width=12,font='Sans 12 bold',command=self.update_function)
        btn_update.grid(row=0,column=2,padx=20,pady=50,sticky=N)

        btn_display=Button(self.bottom,text='DISPLAY',width=12,font='Sans 12 bold',command=self.display_person)
        btn_display.grid(row=0,column=2,padx=20,pady=90,sticky=N)

        btn_delete=Button(self.bottom,text='DELETE',width=12,font='Sans 12 bold',command=self.delete_person)
        btn_delete.grid(row=0,column=2,padx=20,pady=130,sticky=N)

    def add_people(self):
        add_page=AddPeople()
        self.destroy()


    def update_function(self):
        selcted_item=self.listbox.curselection()
        person=self.listbox.get(selcted_item)
        person_id=person[0]
        print(person_id)

        update_page=UpdatePeople(person_id)

    def display_person(self):
        selcted_item=self.listbox.curselection()
        person=self.listbox.get(selcted_item)
        person_id=person[0]

        display_page=DisplayPeople(person_id)

    def delete_person(self):
        selcted_item=self.listbox.curselection()
        person=self.listbox.get(selcted_item)
        person_id=person[0]

        query="delete from addressbook where person_id ={}".format(person_id)
        answer=messagebox.askquestion("Warning",'Are you sure you wanna delete?')
        if answer=='yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo('Succes','Deleted contact')
                self.destroy()
            except Exception as e:
                messagebox.showinfo('Info',str(e))




