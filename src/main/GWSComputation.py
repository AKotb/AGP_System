import Tkinter as tk
import tkFileDialog
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

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
        self.gracesolutionvar = tk.StringVar(self.master)
        self.gracesolutionvar.set("Select Solution")
        gracesolutionnw = tk.OptionMenu(self.master, self.gracesolutionvar, "Select Solution", "CSR", "JPL", "GFZ",
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
        gldasmodelverionnw = tk.OptionMenu(self.master, self.gldasmodelverionvar, "Select Model Version", "CLM",
                                           "MOSAIC", "NOAH",
                                           "VIC", command=self.gldasmodelverionchanged)
        gldasmodelverionnw.grid(sticky='W', padx=10, pady=10, row=3, column=1, columnspan=3)

        # Enter GLDAS Model Version Data File Path
        gldasmodelveriondatafilelbl = tk.Label(self.master, text="GLDAS Model Data File")
        gldasmodelveriondatafilelbl.grid(sticky='W', padx=10, pady=10, row=4, column=0)

        self.gldasmodelveriondatafilefield = tk.Text(self.master, height=1, width=45)
        self.gldasmodelveriondatafilefield.grid(sticky='W', padx=10, pady=10, row=4, column=1, columnspan=2)

        gldasmodelveriondatafilebtn = tk.Button(self.master, text="Browse", command=self.selectgldasmodeldatafile)
        gldasmodelveriondatafilebtn.grid(sticky='W', padx=10, pady=10, row=4, column=3)

        # Enter Surface Water Data File Path
        swdatafilelbl = tk.Label(self.master, text="SW Data File")
        swdatafilelbl.grid(sticky='W', padx=10, pady=10, row=5, column=0)

        self.swdatafilefield = tk.Text(self.master, height=1, width=45)
        self.swdatafilefield.grid(sticky='W', padx=10, pady=10, row=5, column=1, columnspan=2)

        swdatafilebtn = tk.Button(self.master, text="Browse", command=self.selectswdatafile)
        swdatafilebtn.grid(sticky='W', padx=10, pady=10, row=5, column=3)

        # Enter Ground Water Storage output Data File Path
        gwsoutputdatafilelbl = tk.Label(self.master, text="GWS Output Directory")
        gwsoutputdatafilelbl.grid(sticky='W', padx=10, pady=10, row=6, column=0)

        self.gwsoutputdatafilefield = tk.Text(self.master, height=1, width=45)
        self.gwsoutputdatafilefield.grid(sticky='W', padx=10, pady=10, row=6, column=1, columnspan=2)

        gwsoutputdatafilebtn = tk.Button(self.master, text="Browse", command=self.selectgwsoutputdatafile)
        gwsoutputdatafilebtn.grid(sticky='W', padx=10, pady=10, row=6, column=3)

        # control buttons
        self.startcomputinggwsbtn = tk.Button(self.master, text="Compute", width=15, command=self.computegws)
        self.startcomputinggwsbtn.grid(sticky='E', padx=10, pady=10, row=7, column=1)
        self.cancelbtn = tk.Button(self.master, text="Cancel", width=15, command=self.exit)
        self.cancelbtn.grid(sticky='W', padx=10, pady=10, row=7, column=2)

    def exit(self):
        self.master.destroy()

    def gracesolutionchanged(self, selectedgracesolutionvalue):
        # print selectedgracesolutionvalue
        self.gracesolutionvar = selectedgracesolutionvalue

    def gldasmodelverionchanged(self, selectedgldasmodelversionvalue):
        # print selectedgldasmodelversionvalue
        self.gldasmodelverionvar = selectedgldasmodelversionvalue

    def selecttwsdatafile(self):
        self.twsdatafilepath = tkFileDialog.askopenfilename(initialdir="/", title="Select TWS Data File",
                                                            filetypes=(("Excel Sheet", "*.xlsx"), ("All Files", "*.*")))
        self.gracetwsfilefield.delete(1.0, tk.END)
        self.gracetwsfilefield.insert(tk.END, self.twsdatafilepath)

    def selectgldasmodeldatafile(self):
        self.gldasmodeldatafilepath = tkFileDialog.askopenfilename(initialdir="/",
                                                                   title="Select GLDAS Model Version Data File",
                                                                   filetypes=(
                                                                   ("Excel Sheet", "*.xlsx"), ("All Files", "*.*")))
        self.gldasmodelveriondatafilefield.delete(1.0, tk.END)
        self.gldasmodelveriondatafilefield.insert(tk.END, self.gldasmodeldatafilepath)

    def selectswdatafile(self):
        self.swdatafilepath = tkFileDialog.askopenfilename(initialdir="/",
                                                           title="Select SW Data File",
                                                           filetypes=(
                                                               ("Excel Sheet", "*.xlsx"), ("All Files", "*.*")))
        self.swdatafilefield.delete(1.0, tk.END)
        self.swdatafilefield.insert(tk.END, self.swdatafilepath)

    def selectgwsoutputdatafile(self):
        self.gwsoutputdatafilepath = tkFileDialog.askdirectory(initialdir="/", title="Select GWS Output Directory")
        self.gwsoutputdatafilefield.delete(1.0, tk.END)
        self.gwsoutputdatafilefield.insert(tk.END, self.gwsoutputdatafilepath)

    def computegws(self):
        selectedgracesolution = self.gracesolutionvar
        # print selectedgracesolution

        enteredtwsdatafilepath = self.gracetwsfilefield.get("1.0", tk.END)
        if (enteredtwsdatafilepath.endswith("\n")):
            enteredtwsdatafilepath = enteredtwsdatafilepath[:-1]
        twsdf = pd.read_excel(enteredtwsdatafilepath, sheet_name='Sheet1')
        # print(twsdf.columns)
        listGraceJPLData = twsdf[selectedgracesolution+'_TWS']
        monthsList = twsdf['Month']
        # print(len(listGraceJPLData))

        selectedgldasmodelverion = self.gldasmodelverionvar
        # print selectedgldasmodelverion

        enteredgldasmodeldatafilepath = self.gldasmodelveriondatafilefield.get("1.0", tk.END)
        if (enteredgldasmodeldatafilepath.endswith("\n")):
            enteredgldasmodeldatafilepath = enteredgldasmodeldatafilepath[:-1]
        gldasdf = pd.read_excel(enteredgldasmodeldatafilepath, sheet_name='Sheet1')
        # print(gldasdf.columns)
        listGLDASData = gldasdf[selectedgldasmodelverion+'_TWS']
        # print(len(listGLDASData))

        enteredswdatafilepath = self.swdatafilefield.get("1.0", tk.END)
        if (enteredswdatafilepath.endswith("\n")):
            enteredswdatafilepath = enteredswdatafilepath[:-1]
        swsdf = pd.read_excel(enteredswdatafilepath, sheet_name='Sheet1')
        # print(swsdf.columns)
        listSWSData = swsdf['SWS']
        # print(len(listSWSData))

        enteredgwsoutputdatafilepath = self.gwsoutputdatafilefield.get("1.0", tk.END)
        if (enteredgwsoutputdatafilepath.endswith("\n")):
            enteredgwsoutputdatafilepath = enteredgwsoutputdatafilepath[:-1]

        gwsdf = listGraceJPLData - listGLDASData - listSWSData
        formattedgwsdf = pd.DataFrame({'GWS': gwsdf, 'Month': monthsList})
        writer = pd.ExcelWriter(enteredgwsoutputdatafilepath+'/Net_GWS_Generated.xlsx', engine='xlsxwriter')
        formattedgwsdf.to_excel(writer, sheet_name='sheet1', index=False)
        writer.save()
        writer.close()

        self.startcomputinggwsbtn.grid_forget()
        self.cancelbtn.grid_forget()

        self.closecomputinggwsbtn = tk.Button(self.master, text="Close", width=15, command=self.exit)
        self.closecomputinggwsbtn.grid(sticky='E', padx=10, pady=10, row=7, column=1)
        self.startnewgwsbtn = tk.Button(self.master, text="New GWS Window", width=15, command=self.reset)
        self.startnewgwsbtn.grid(sticky='W', padx=10, pady=10, row=7, column=2)

    def reset(self):
        self.master.destroy()
        root = tk.Tk()
        root.geometry("650x400")
        GWSComputation(root)
        root.mainloop()