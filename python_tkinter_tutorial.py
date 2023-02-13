from tkinter import*
from tkinter import filedialog

# Lesson 1:
#------------
# every item is a widget
# root is the main widget like body in te HTML

# creating a root widget 
root = Tk() 
# create a widget and put it into the root widget
myLabel = Label(root, text ='ez egy vidzsit')
# Shoving the created widget onto the screen
myLabel.pack()
# close the loop
root.mainloop()

# Lesson 2.:
#-----------------------------
# grid system
root = Tk()
myLabel1 = Label(root, text="----").grid(grid=0, column=0)
myLabel2 = Label(root, text="kkkk").grid(grid=1, column=1)
'''
myLabel1
myLabel2.grid(grid=1, column=1)
'''
root.mainloop()

# Lesson 3-4.:
#-----------------------------
# button, inputFields
root = Tk()
e = Entry(root, width=50, bg="blue")
e.pack()

def myClick():
    myLabel1 = Label(root, text='Aj klkked hir')
    myLabel1.pack()

myButton = Button(root, text='button', state=DISABLED, padx=50, pady=100, command=myClick(), fg="blue", bg="red")
myButton.pack()

root.mainloop()

# Lesson 5:
#--------------------------------
# get(), title, radio, status

root = Tk()
root.title('Ez a root cime')
root.iconbitmap('c:/gui/codemy.ico')
root.filename = filedialog.askopenfilename(initialdir="/gui/images", title='Select a file', filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"))) 
e = Entry(root, width=50, bg="blue")
e.pack()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, volume=mode).pack(anchor=")


def clicked(value):
    myLabel1 = Label(root, text=value)
    myLabel1.pack()

# Lambda function and get() method used in command
myButton = Button(root, text='button', state=DISABLED, padx=50, pady=100, command=Lambda: clicked(e.get()), fg="blue", bg="red")
myButton.pack()

root.mainloop()



