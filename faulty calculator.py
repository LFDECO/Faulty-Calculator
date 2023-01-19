import tkinter as tk
import random
#creating a class to keep all the gui methods together and calling the class at the end which call the func as well
light_black="#F5F5F5"
lcolor="#25265E"
white="#FFFFFF"
mainfont=("Opera Sans",40,"bold")
fontstyle=("Opera Sans",16)
dfont=("Opera Sans",24,"bold")
opfont=("Opera Sans",20)
class calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Faulty Calculator")
        self.total=""
        self.current=""
        self.digit={7:(1,1),8:(1,2),9:(1,3),
                    4:(2,1),5:(2,2),6:(2,3),
                    1:(3,1),2:(3,2),3:(3,3),
                    0:(4,2),'.':(4,1)
                    }
        self.operation={"/": "\u00F7", "*": "\u00D7","-":"-","+":"+"}
        self.dispframe=self.dispframe()
        self.buttonframe=self.buttonframe()
        self.buttonframe.rowconfigure(0,weight=1)
        for i in range(1,5):
            self.buttonframe.rowconfigure(i,weight=1)
            self.buttonframe.columnconfigure(i,weight=1)
        self.digit_buttons()
        self.operatorbutton()
        self.createclear()
        self.equal()
        self.all_label,self.tlabel=self.label()
    def label(self):
        all_label=tk.Label(self.dispframe,text=self.total,anchor=tk.E,bg=lcolor,fg=light_black,padx=24,font=fontstyle)
        all_label.pack(expand=True,fill="both")
        tlabel=tk.Label(self.dispframe,text=self.current,anchor=tk.E,bg=lcolor,fg=light_black,padx=24,font=mainfont)
        tlabel.pack(expand=True,fill="both")
        return all_label,tlabel
    def dispframe(self):
       frame=tk.Frame(self.window,height=221,bg=light_black)
       frame.pack(expand=True,fill="both")
       return frame
    def digit_buttons(self):
        for digits,gridval in self.digit.items():
            button=tk.Button(self.buttonframe,text=str(digits),bg=white,fg=lcolor,font=dfont,borderwidth=0,command=lambda x=digits: self.add(x))
            button.grid(row=gridval[0],column=gridval[1],sticky=tk.NSEW)
        
    def operatorbutton(self):
        i=0
        for operator,symbol in self.operation.items():
            button=tk.Button(self.buttonframe,text=symbol,bg=lcolor,fg=white,font=opfont,borderwidth=0,command=lambda x=operator: self.operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def createclear(self):
        button=tk.Button(self.buttonframe,text="C",bg=lcolor,fg=white,font=opfont,borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,columnspan=3,sticky=tk.NSEW)
    def equal(self):
        button=tk.Button(self.buttonframe,text="=",bg=lcolor,fg=white,font=opfont,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)
    def buttonframe(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    def updatelabel(self):
        self.all_label.config(text=self.total)
    def updatecurrent(self):
        self.tlabel.config(text=self.current) 
    def add(self,value):
        self.current+=str(value)
        self.updatecurrent()
    def operator(self,op):
        self.current+=op
        self.total+=self.current
        self.current="" 
        self.updatelabel()
        self.updatecurrent()  
    def clear(self):
        self.current=""
        self.total=""
        self.updatecurrent()
        self.updatelabel()
    def evaluate(self):
        #introducing error
        self.total+=self.current
        self.updatelabel()
        if random.randint(1,5)==1 or random.randint(1,5)==2:
            self.current=str(eval(self.total)*2)
            self.total=""
            self.updatecurrent()
        else:
            self.current=str(eval(self.total))
            self.total=""
            self.updatecurrent()
    def start(self):
        self.window.mainloop()
calc=calculator()
calc.start()