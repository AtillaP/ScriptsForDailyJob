from gui import Gui
from swdata import Sw

def Main():
    app = Gui()
    app.mainloop()
    ssw = Sw(app.getSWName())
    print(ssw.getSWName())
    
if __name__ == '__main__':
    Main()