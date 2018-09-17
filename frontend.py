"""
A Program that stores book's information.

Front-End:
    Text (Entry Widgets) Fields: Title, Author, Year, ISBN
    User can view all records, search entry, update entry, delete entry, exit (program).

Back-End:
    Entry Widget
    Scroll Bar
    Command Buttons
    Tkinter -> Grid Method
"""

from tkinter import *
from backend import Database # importing the class

database = Database("books.db")

window = Tk()
class Window(object):

    def __init__(self,window):
        self.window = window
        self.window.wm_title("Book Store")


        l1=Label(window,text="Title")
        l1.grid(row=0,column=0)

        l2=Label(window,text="Author")
        l2.grid(row=0,column=2)

        l3=Label(window,text="Year")
        l3.grid(row=1,column=0)

        l4=Label(window,text="ISBN")
        l4.grid(row=1,column=2)

        self.title_text=StringVar()
        self.e1=Entry(window,textvariable=self.title_text)
        self.e1.grid(row=0,column=1)

        self.author_text=StringVar()
        self.e2=Entry(window,textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e3=Entry(window,textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        # bind method for the delete_command
        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        b1=Button(window, text='View All', width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2=Button(window, text='Search Entry', width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3=Button(window, text='Add Entry', width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4=Button(window, text='Update Selected', width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5=Button(window, text='Delete Selected', width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6=Button(window, text='Close', width=12,  command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self,event):
        
        #global selected_tuple
        # identifies the index of the user selected item in the list1. 
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)
    
        # Shows in the entry fields the user selected row item.
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1]) # title has the index of 1
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2]) # title has the index of 1
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3]) # title has the index of 1
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4]) # title has the index of 1    
        #print(selected_tuple)

    def view_command(self):
        # ensures that everything is deleted from 0 to the end (last row). Pressing 'view all' does not repeatedly shows the same results.
        self.list1.delete(0,END)
        for row in database.view():
            # the new rows will be added at the end of the exisiting rows. Ensures that every new rows are added at the end.
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0, END)
        # uses get for a search method.
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        # adds the entry to the database.
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        # makes sure the list is empty
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        # once the user selects the row, we need to identify the ID and get it deleted.
        database.delete(self.selected_tuple[0])

    def update_command():
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])

Window(window)
window.mainloop()
