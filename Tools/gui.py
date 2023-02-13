from tkinter import*
from tkinter import filedialog

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.title("SWAnalyzer")
        self.geometry("400x250")
        self.swbutton = Button(self, text="Choose SW")
        self.SWName = None
        self.swbutton['command'] = self.chooseSW
        self.swbutton.pack()
    def setSWName(self, name):
        self.SWName = name
    def chooseSW(self):
        self.setSWName(str(filedialog.askdirectory(initialdir="D:/SAFE handling")))
        self.swNameEntry = Entry(self, )
    def getSWName(self):
        return self.SWName