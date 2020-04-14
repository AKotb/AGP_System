import os
from subprocess import *
import subprocess
import tkFileDialog

import Tkinter as tk


class ZonalStatistics(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Zonal Statistics")
        self.pack(fill=tk.BOTH, expand=1)
        
        inputrasterdatadirlbl = tk.Label(self.master, text="Input Raster Data")
        inputrasterdatadirlbl.place(x=20, y=50)
        self.inputrasterdatadirtxtfield = tk.Text(self.master, height=1, width=50)
        self.inputrasterdatadirtxtfield.place(x=130, y=50)
        inputrasterdatadirbtn = tk.Button(self.master, text="Browse", command=self.selectrasterdatadir)
        inputrasterdatadirbtn.place(x=540, y=47)
        
        outputtabledatadirlbl = tk.Label(self.master, text="Output Table")
        outputtabledatadirlbl.place(x=20, y=100)
        self.outputtabledatadirtxtfield = tk.Text(self.master, height=1, width=50)
        self.outputtabledatadirtxtfield.place(x=130, y=100)
        outputtabledatadirbtn = tk.Button(self.master, text="Browse", command=self.selectoutputtabledatadir)
        outputtabledatadirbtn.place(x=540, y=97)
        
        featurezonelbl = tk.Label(self.master, text="Feature Zone")
        featurezonelbl.place(x=20, y=150)
        self.featurezonetxtfield = tk.Text(self.master, height=1, width=50)
        self.featurezonetxtfield.place(x=130, y=150)
        featurezonebtn = tk.Button(self.master, text="Browse", command=self.selectfeaturezone)
        featurezonebtn.place(x=540, y=147)

        self.startbtn = tk.Button(self.master, text="Start", command=self.startzonalstatistics)
        self.startbtn.place(x=500, y=200)
        self.cancelbtn = tk.Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.place(x=540, y=200)

    def exit(self):
        self.master.destroy()

    def selectrasterdatadir(self):
        self.inputrasterdatapath = tkFileDialog.askdirectory(initialdir="/", title="Select Raster Data Directory")
        self.inputrasterdatadirtxtfield.delete(1.0, tk.END)
        self.inputrasterdatadirtxtfield.insert(tk.END, self.inputrasterdatapath)
        
    def selectoutputtabledatadir(self):
        self.outputtablepath = tkFileDialog.askdirectory(initialdir="/", title="Select Output Table Directory")
        self.outputtabledatadirtxtfield.delete(1.0, tk.END)
        self.outputtabledatadirtxtfield.insert(tk.END, self.outputtablepath)
        
    def selectfeaturezone(self):
        self.featurezonepath = tkFileDialog.askopenfilename(initialdir="/", title="Select Feature Zone",
                                                        filetypes=(("Shp Files", "*.shp"), ("All Files", "*.*")))
        self.featurezonetxtfield.delete(1.0, tk.END)
        self.featurezonetxtfield.insert(tk.END, self.featurezonepath)

    def startzonalstatistics(self):
        #inputrasterdata = self.inputrasterdatadirtxtfield.get("1.0", tk.END)
        #inputrasterdata = "-i "+inputrasterdata
        inputrasterdata = r"-i D:/NARSS/Research Project/2018-2019/01-01-2020/Land_Surface_Models_Tasks/Task2_SUM_TIFFs_Output/CLM"
        print "inputrasterdata: "+inputrasterdata

        #outputtable = self.outputtabledatadirtxtfield.get("1.0", tk.END)
        #outputtable = "-o "+outputtable
        outputtable = r"-o D:/NARSS/Research Project/2018-2019/01-01-2020/Land_Surface_Models_Tasks/Task3_Zonal-Statistics_Output/CLM"
        print "outputtable: "+outputtable

        #featurezone = self.featurezonetxtfield.get("1.0", tk.END)
        #featurezone = "-f "+featurezone
        featurezone = r"-f D:/NARSS/Research Project/2018-2019/01-01-2020/Land_Surface_Models_Tasks/Nile_basin_shp/Features-polygon.shp"
        print "featurezone: "+featurezone

        # ArcGIS Python Interpreter
        arcgisinterpreter = r"C:\Python27\ArcGIS10.4\python.exe"

        # Zonal Statistics business script
        zonalstatistics_script = r"C:\Users\ahmed.kotb\PycharmProjects\AGPS\src\main\Zonal_Statistics_Script.py"

        command = 'cmd /k {0} {1} "{2}" "{3}" "{4}"'.format(arcgisinterpreter, zonalstatistics_script, inputrasterdata,
                                                            outputtable, featurezone)
        os.system(command)
