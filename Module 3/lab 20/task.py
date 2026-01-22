from tkinter import *
import re



class Main(Frame):
    def __init__(self,root):
        super(Main,self).__init__(root)
        self.build()
    def safe_eval(self, expr):
        if re.fullmatch(r"[0-9+\-*/%.]+", expr):
            return str(eval(expr))
        return "Error"
    def build(self):
        self.formula= ""
        self.label= Label(text=self.formula,font=('Arial',30),bg="#000",foreground="#FFF")
        self.label.place(x=11,y=50)
        btns=[
            'C','<-','%','/',
            '7','8','9','*',
            '4','5','6','-',
            '1','2','3','+',
            '0','.','=',''
        ]
        a=10
        b=140
        for btn in btns:
            command= lambda x=btn: self.logical(x)
            Button(text=btn,command=command,width=5,height=2,bg='#FFF',font=('Arial',15)).place(x=a,y=b,width=115,height=79)
            a+=117
            if a>400:
                a=10
                b+=81

    def logical(self,operation):
        if len(self.formula) > 15:
            return
        if operation=='C':
            self.formula=''
        elif operation=='<-':
            self.formula=self.formula[:-1]
            if self.formula=='':
                self.formula=''
        elif operation == '=':
            self.formula = self.safe_eval(self.formula)
        else:
            if self.formula=='':
                self.formula=''
            self.formula+=operation
        if operation in '+-*/%' and self.formula[-1] in '+-*/%':
            return
        self.update()

    def update(self):
        if self.formula=='0':
            self.formula=''
        self.label.config(text=self.formula)

   
if __name__ == '__main__':
   root = Tk()
   root["bg"] = "#000"
   root.geometry('485x550+200+200')
   root.title('Calculator')
   root.resizable(False, False)

   app = Main(root)
   app.pack()

   root.mainloop()