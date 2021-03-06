from tkinter import *
import pyperclip
from tkinter import filedialog

root=Tk()
root.title("Notepad")

def copy_to_clipboard():
	pyperclip.copy(text.get("1.0","end-1c"))
	
def clear():
	text.delete(1.0,'end')
	
def save():
	opf=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
	if opf is None:
		return
	entry=str(text.get(1.0,END))
	opf.write(entry)
	opf.close()
	
def openF():
	f=filedialog.askopenfile(mode='r')
	if f is not None:
		cont=f.read()
	text.insert(INSERT,cont)

text=Text(root,width=200,height=50)
button1=Button(root,text="Copy",command=copy_to_clipboard)
button2=Button(root,text="Clear",command=clear)
button3=Button(root,text="Quit",command=root.destroy)
button4=Button(root,text="Open",command=openF)
button5=Button(root,text="Save",command=save)

text.grid(row=2,columnspan=5,sticky=W+E+N+S)
button1.grid(row=1,column=1,sticky=W+E+N+S)
button2.grid(row=1,column=2,sticky=W+E+N+S)
button3.grid(row=1,column=4,sticky=W+E+N+S)
button4.grid(row=1,column=0,sticky=W+E+N+S)
button5.grid(row=1,column=3,sticky=W+E+N+S)

root.mainloop()
