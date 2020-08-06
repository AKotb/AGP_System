import os

import tkFileDialog
import Tkinter as tk
import batch_zonal_stats as zs


class ZonalStatistics(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        # window title in the title bar
        self.master.title("Zonal Statistics")

        # window title label
        windowlbl = tk.Label(self.master, text="Zonal Statistics")
        windowlbl.grid(padx=10, pady=10, row=0, column=0, columnspan=4)

        # Raster Data Directory
        inputrasterdatadirlbl = tk.Label(self.master, text="Input Raster Data")
        inputrasterdatadirlbl.grid(sticky='W', padx=10, pady=10, row=1, column=0)
        self.inputrasterdatadirtxtfield = tk.Text(self.master, height=1, width=50)
        self.inputrasterdatadirtxtfield.grid(sticky='W', padx=10, pady=10, row=1, column=1, columnspan=2)
        inputrasterdatadirbtn = tk.Button(self.master, text="Browse", command=self.selectrasterdatadir)
        inputrasterdatadirbtn.grid(sticky='W', padx=10, pady=10, row=1, column=3)
        
        outputtabledatadirlbl = tk.Label(self.master, text="Output Table")
        outputtabledatadirlbl.grid(sticky='W', padx=10, pady=10, row=2, column=0)
        self.outputtabledatadirtxtfield = tk.Text(self.master, height=1, width=50)
        self.outputtabledatadirtxtfield.grid(sticky='W', padx=10, pady=10, row=2, column=1, columnspan=2)
        outputtabledatadirbtn = tk.Button(self.master, text="Browse", command=self.selectoutputtabledatadir)
        outputtabledatadirbtn.grid(sticky='W', padx=10, pady=10, row=2, column=3)
        
        featurezonelbl = tk.Label(self.master, text="Feature Zone")
        featurezonelbl.grid(sticky='W', padx=10, pady=10, row=3, column=0)
        self.featurezonetxtfield = tk.Text(self.master, height=1, width=50)
        self.featurezonetxtfield.grid(sticky='W', padx=10, pady=10, row=3, column=1, columnspan=2)
        featurezonebtn = tk.Button(self.master, text="Browse", command=self.selectfeaturezone)
        featurezonebtn.grid(sticky='W', padx=10, pady=10, row=3, column=3)

        self.startbtn = tk.Button(self.master, text="Start", command=self.startzonalstatistics)
        self.startbtn.grid(sticky='E', padx=10, pady=10, row=4, column=1)
        self.cancelbtn = tk.Button(self.master, text="Cancel", command=self.exit)
        self.cancelbtn.grid(sticky='W', padx=10, pady=10, row=4, column=2)

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
        inputrasterdata = self.inputrasterdatadirtxtfield.get("1.0", tk.END)
        inputrasterdata = inputrasterdata.encode('ascii', 'ignore')
        #inputrasterdata = r"D:/NARSS/Research_Project/2018-2019/01-01-2020/Land_Surface_Models_Tasks/Task2_SUM_TIFFs_Output/CLM"
        print "inputrasterdata: "+inputrasterdata

        outputtable = self.outputtabledatadirtxtfield.get("1.0", tk.END)
        outputtable = outputtable.encode('ascii', 'ignore')
        #outputtable = r"D:/NARSS/Research_Project/2018-2019/01-01-2020/Land_Surface_Models_Tasks/Task3_Zonal-Statistics_Output/CLM"
        print "outputtable: "+outputtable

        featurezone = self.featurezonetxtfield.get("1.0", tk.END)
        featurezone = featurezone.encode('ascii', 'ignore')
        #featurezone = r"D:/NARSS/Research_Project/2018-2019/01-01-2020/Land_Surface_Models_Tasks/Nile_basin_shp/Features-polygon.shp"
        print "featurezone: "+featurezone

        zs.batch_calculate_zonal_stats(inputrasterdata, outputtable, featurezone)

        '''
        # ArcGIS Python Interpreter
        arcgisinterpreter = r"C:\Python27\ArcGIS10.4\python.exe"

        # Zonal Statistics business script
        zonalstatistics_script = r"C:\Users\ahmed.kotb\PycharmProjects\AGPS\src\main\Zonal_Statistics_Script.py"

        command = 'cmd /k {0} {1} "{2}" "{3}" "{4}"'.format(arcgisinterpreter, zonalstatistics_script, inputrasterdata,
                                                            outputtable, featurezone)
        os.system(command)
        '''
