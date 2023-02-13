import os
from tkinter import filedialog
from tkinter import ttk
from tkinter import*

global file_path

def browse_button():
    folder_path = filedialog.askopenfilename()

def Main():

    root = Tk()
    root.title("FileHandler")
    root.geometry("350x100")

    file_path = StringVar()


    Label(frame, textvariable=file_path, width = 20).pack()
    
    browseButton = Button(text="BrowseFolder", command=browse_button)
    browseButton.grid(row=0, column=3)
    
    #frame.pack()
    root.mainloop()


if __name__ == "__main__":
    Main()