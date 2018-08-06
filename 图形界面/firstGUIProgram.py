from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.creatWidgets()
    
    def creatWidgets(self):
        self.helloLabel = Label(self,text='Hello,world!')
        self.helloLabel.pack()
        self.qutiButton = Button(self,text='Quit',command=self.quit)
        self.qutiButton.pack()

app = Application()     
app.master.title('hello world')
app.mainloop()