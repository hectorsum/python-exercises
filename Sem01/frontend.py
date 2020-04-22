#Importing everything from tkinter
import tkinter as tk
#from tkinter.ttk import *
#Create Windows object
window = tk.Tk()
#Defining out labels        
l1 = tk.Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = tk.Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = tk.Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = tk.Label(window,text="ISBN")
l4.grid(row=1,column=2)

#Defining Entries
title_text = tk.StringVar()
e1 = tk.Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = tk.StringVar()
e2 = tk.Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = tk.StringVar()
e3 = tk.Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = tk.StringVar()
e4 = tk.Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#Defining ListBox
list1 = tk.Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Attach scrollbar to the List
sb1 = tk.Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6) #Row span allows to enlarge the box vertically(6),which is the height of the listbox

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Defining buttons
b1 = tk.Button(window,text="View All",width=12)
b1.grid(row=2,column=3)

b2 = tk.Button(window,text="Search Entry",width=12)
b2.grid(row=3,column=3)

b3 = tk.Button(window,text="Add Entry",width=12)
b3.grid(row=4,column=3)

b4 = tk.Button(window,text="Update selected",width=12)
b4.grid(row=5,column=3)

b4 = tk.Button(window,text="Delete selected",width=12)
b4.grid(row=6,column=3)

b5 = tk.Button(window,text="Close",width=12)
b5.grid(row=7,column=3)


window.mainloop()
