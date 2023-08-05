from tkinter import *
import math

def click(event):
   global scvalue
   text = event.widget.cget("text")
   print(text)
   if text == "=":
      if scvalue.get().isdigit():
         value = int(scvalue.get())
      else:
         value = eval(scvalue.get())

         scvalue.set(value)
         screen.update()
         
   elif text == "C":
      scvalue.set("")
      screen.update()

   elif text == "CE":  # Adding CE functionality
        current_text = scvalue.get()
        if current_text:
            new_text = current_text[:-1]  # Remove the last character
            scvalue.set(new_text)

   else:
      scvalue.set(scvalue.get() + text)
      screen.update()

root = Tk()

root.geometry("644x900")
root.title("Calculator By Saif")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X, ipadx=8 , pady=10, padx=10)


f = Frame(root , bg="grey")
b = Button(f, text="C", padx=17.5, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=10.35, pady=5)
b.bind("<Button-1>" , click)


b = Button(f, text="CE", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=8.7, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="*", padx=8.7, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=10, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="±", padx=17.5, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=10.35, pady=5)
b.bind("<Button-1>" , click)

f.pack()

f = Frame(root , bg="grey")
b = Button(f, text="7", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>" , click)


b = Button(f, text="8", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="9", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="-", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15, pady=5)
b.bind("<Button-1>" , click)

f.pack()

f = Frame(root , bg="grey")
b = Button(f, text="4", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=13.5, pady=5)
b.bind("<Button-1>" , click)


b = Button(f, text="5", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=13.5, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="6", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=13.5, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="+", padx=14, pady=17, font="lucida 30 bold")
b.pack(side=LEFT,  padx=13.5, pady=5)
b.bind("<Button-1>" , click)

f.pack()

f = Frame(root , bg="grey")
b = Button(f, text="1", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=15.2, pady=5)
b.bind("<Button-1>" , click)


b = Button(f, text="2", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15.2, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="3", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15.2, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="/", padx=16, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15.2, pady=5)
b.bind("<Button-1>" , click)

f.pack()

f = Frame(root , bg="grey")
b = Button(f, text="%", padx=14, pady=18, font="lucida 30 bold")
b.pack(side=LEFT, padx=14.5, pady=5)
b.bind("<Button-1>" , click)


b = Button(f, text="0", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text=".", padx=15, pady=18, font="lucida 30 bold")
b.pack(side=LEFT,  padx=15, pady=5)
b.bind("<Button-1>" , click)

b = Button(f, text="=", padx=13.5, pady=17, font="lucida 30 bold")
b.pack(side=LEFT,  padx=12.3, pady=5)
b.bind("<Button-1>" , click)

f.pack()




root.mainloop()