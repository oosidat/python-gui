## A Basic Compound Interest Calculator

import Tkinter

class compintapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        ## Title & subtitle labels ---------------------------------------
        titlelbl = Tkinter.Label(self, text="Basic Compound Interest Calculator",
                              anchor="center",fg="white",bg="red")
        titlelbl.grid(column=0,row=0,columnspan=3,sticky='EW')
        
        subtitlelbl = Tkinter.Label(self, text="By Osama Sidat",
                              anchor="center",fg="white",bg="black")
        subtitlelbl.grid(column=0,row=1,columnspan=3,sticky='EW')
        
        ## end of title & subtitle lbls ----------------------------------
        
        ## Input Labels --------------------------------------------------
        
        principallbl = Tkinter.Label(self, text="Principal :",
                              anchor="w",fg="white",bg="SlateGray4")
        principallbl.grid(column=0,row=2,columnspan=1,sticky='EW')
        
        intratelbl = Tkinter.Label(self, text="Rate of Interest (Annual Percentage) :",
                              anchor="w",fg="white",bg="SlateGray4")
        intratelbl.grid(column=0,row=3,columnspan=1,sticky='EW')
        
        timescomplbl = Tkinter.Label(self, text="Number of Times Compounded Per Year :",
                              anchor="w",fg="white",bg="SlateGray4")
        timescomplbl.grid(column=0,row=4,columnspan=1,sticky='EW')
        
        yrslbl = Tkinter.Label(self, text="Number of Years :",
                              anchor="w",fg="white",bg="SlateGray4")
        yrslbl.grid(column=0,row=5,columnspan=1,sticky='EW')
        
        amountlbl = Tkinter.Label(self, text="Total Amount :",
                              anchor="w",fg="white",bg="SlateGray4")
        amountlbl.grid(column=0,row=7,columnspan=1,sticky='EW')
        
        earnlbl = Tkinter.Label(self, text="Total Interest Earned :",
                              anchor="w",fg="white",bg="SlateGray4")
        earnlbl.grid(column=0,row=8,columnspan=1,sticky='EW')
        
        
        ## end of input labels ------------------------------------------------
        
        ## Input Boxes --------------------------------------------------------
        #self.pr = Tkinter.DoubleVar()
        #principal = Tkinter.Entry(self,textvariable=self.pr)
        #principal.grid(column=1,row=2,sticky='EW')
        
        self.pr = Tkinter.DoubleVar()
        principal = Tkinter.Entry(self,textvariable=self.pr)
        principal.grid(column=1,row=2, sticky='EW')
                
        self.rate = Tkinter.DoubleVar()
        intrate = Tkinter.Entry(self,textvariable=self.rate)
        intrate.grid(column=1,row=3, sticky='EW')
                
        self.ntimes = Tkinter.IntVar()
        times = Tkinter.Entry(self,textvariable=self.ntimes)
        times.grid(column=1,row=4, sticky='EW')
        
        self.years = Tkinter.DoubleVar()
        yrs = Tkinter.Entry(self,textvariable=self.years)
        yrs.grid(column=1,row=5, sticky='EW')
                
        ## end of input boxes -------------------------------------------------
        
        ## Button
        button = Tkinter.Button(self,text="C A L C U L A T E",
                                command=self.OnButtonClick)
        button.grid(column=0,row=6,columnspan=3)
        ## end of button
        
        ## Output labels
        self.amt = Tkinter.StringVar()
        amtout = Tkinter.Label(self,textvariable=self.amt,
                              anchor="e",fg="red",bg="yellow")
        amtout.grid(column=1,row=7,columnspan=2,sticky='EW')
        
        self.earn = Tkinter.StringVar()
        earnout = Tkinter.Label(self,textvariable=self.earn,
                              anchor="e",fg="red",bg="gold")
        earnout.grid(column=1,row=8,columnspan=2,sticky='EW')
        ## end of output labels -----------------------------------------------
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)


    def OnButtonClick(self):
        p = self.pr.get()
        i = self.rate.get()
        t = self.ntimes.get()
        y = self.years.get()
        
        ## Compound Interest Calculation
        amount = round((p * ((1 + ((i/100) / t))**(t * y))),2)
        intearn = round((amount - p),2)
        self.amt.set(amount)
        self.earn.set(intearn)
        
if __name__ == "__main__":
    app = compintapp_tk(None)
    app.title('Basic Compound Interest Calculator')
    app.mainloop()

    
## Notes:
## anchor for title at 'centre'