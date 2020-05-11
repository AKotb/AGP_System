import os
import tkFileDialog
import Tkinter as tk
from pymatbridge import Matlab


class GWSComputation(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # window title in the title bar
        self.master.title("Ground Water Storage Computation")
        
        # window title label
        windowlbl = tk.Label(self.master, text="Ground Water Storage Computation")
        windowlbl.grid(padx=10, pady=10, row=0, column=0, columnspan=4)
        
        # Select GRACE Solution
        gracesolutionlbl = tk.Label(self.master, text="GRACE Solution")
        gracesolutionlbl.grid(sticky='W', padx=10, pady=10, row=1, column=0)
        self. gracesolutionvar = tk.StringVar(self.master)
        self. gracesolutionvar.set("Select Solution")
        gracesolutionnw = tk.OptionMenu(self.master, self. gracesolutionvar, "Select Solution", "CSR", "JPL", "GFZ",
                                           "Harmonics", command=self.gracesolutionchanged)
        gracesolutionnw.grid(sticky='W', padx=10, pady=10, row=1, column=1, columnspan=3)

        # Enter TWS Data File Path
        gracetwsfilelbl = tk.Label(self.master, text="GRACE TWS File")
        gracetwsfilelbl.grid(sticky='W', padx=10, pady=10, row=2, column=0)

        self.gracetwsfilefield = tk.Text(self.master, height=1, width=45)
        self.gracetwsfilefield.grid(sticky='W', padx=10, pady=10, row=2, column=1, columnspan=2)

        gracetwsfilebtn = tk.Button(self.master, text="Browse", command=self.selecttwsdatafile)
        gracetwsfilebtn.grid(sticky='W', padx=10, pady=10, row=2, column=3)

        # Select GLDAS Model Version
        gldasmodelverionlbl = tk.Label(self.master, text="GLDAS Model Version")
        gldasmodelverionlbl.grid(sticky='W', padx=10, pady=10, row=3, column=0)
        self.gldasmodelverionvar = tk.StringVar(self.master)
        self.gldasmodelverionvar.set("Select Model Version")
        gldasmodelverionnw = tk.OptionMenu(self.master, self.gldasmodelverionvar, "Select Model Version", "CLM", "MOSAIC", "NOAH",
                                        "VIC", command=self.gldasmodelverionchanged)
        gldasmodelverionnw.grid(sticky='W', padx=10, pady=10, row=3, column=1, columnspan=3)

        # Enter GLDAS Model Version Data File Path
        gldasmodelveriondatafilelbl = tk.Label(self.master, text="GLDAS Model Data File")
        gldasmodelveriondatafilelbl.grid(sticky='W', padx=10, pady=10, row=4, column=0)

        self.gldasmodelveriondatafilefield = tk.Text(self.master, height=1, width=45)
        self.gldasmodelveriondatafilefield.grid(sticky='W', padx=10, pady=10, row=4, column=1, columnspan=2)

        gldasmodelveriondatafilebtn = tk.Button(self.master, text="Browse", command=self.selectgldasmodeldatafile)
        gldasmodelveriondatafilebtn.grid(sticky='W', padx=10, pady=10, row=4, column=3)


    def exit(self):
        self.master.destroy()

    def selecttwsdatafile(self):
        print 'selecttwsdatafile fucntion'

    def selectgldasmodeldatafile(self):
        print 'selectgldasmodeldatafile function'
        