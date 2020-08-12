import tkFileDialog
import Tkinter as tk
import ndwi_tiff_modis


class NDWIComputationFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # window title in the title bar
        self.master.title("Computing NDWI")

        # window title label
        windowlbl = tk.Label(self.master, text="Computing NDWI")
        windowlbl.grid(padx=10, pady=10, row=0, column=0, columnspan=4)

        # Enter Input Data Directory
        inputdatadirlbl = tk.Label(self.master, text="Input Data Directory")
        inputdatadirlbl.grid(sticky='W', padx=10, pady=10, row=1, column=0)
        self.inputdatadirfield = tk.Text(self.master, height=1, width=45)
        self.inputdatadirfield.grid(sticky='W', padx=10, pady=10, row=1, column=1, columnspan=2)
        inputdatadirbtn = tk.Button(self.master, text="Browse", command=self.selectinputdatadir)
        inputdatadirbtn.grid(sticky='W', padx=10, pady=10, row=1, column=3)

        # NIR Band Order
        nirbandorderlbl = tk.Label(self.master, text="NIR Band Order")
        nirbandorderlbl.grid(sticky='W', padx=10, pady=10, row=2, column=0)
        self.nirbandordervar = tk.StringVar(self.master)
        self.nirbandordervar.set("1")
        nirbandordernw = tk.OptionMenu(self.master, self.nirbandordervar, "1", "2", "3", "4",
                                        "5", "6", "7", command=self.nirbandorderchanged)
        nirbandordernw.grid(sticky='W', padx=10, pady=10, row=2, column=1, columnspan=3)

        # SWIR Band Order
        swirbandorderlbl = tk.Label(self.master, text="SWIR Band Order")
        swirbandorderlbl.grid(sticky='W', padx=10, pady=10, row=3, column=0)
        self.swirbandordervar = tk.StringVar(self.master)
        self.swirbandordervar.set("1")
        swirbandordernw = tk.OptionMenu(self.master, self.swirbandordervar, "1", "2",
                                           "3", "4", "5", "6", "7", command=self.swirbandorderchanged)
        swirbandordernw.grid(sticky='W', padx=10, pady=10, row=3, column=1, columnspan=3)

        # Output NDWI Directory
        outputndwidirlbl = tk.Label(self.master, text="Output NDWI Directory")
        outputndwidirlbl.grid(sticky='W', padx=10, pady=10, row=4, column=0)
        self.outputndwidirfield = tk.Text(self.master, height=1, width=45)
        self.outputndwidirfield.grid(sticky='W', padx=10, pady=10, row=4, column=1, columnspan=2)
        outputndwidirbtn = tk.Button(self.master, text="Browse", command=self.selectoutputndwidir)
        outputndwidirbtn.grid(sticky='W', padx=10, pady=10, row=4, column=3)

        # control buttons
        self.startcomputingndwibtn = tk.Button(self.master, text="Compute", width=15, command=self.computendwi)
        self.startcomputingndwibtn.grid(sticky='E', padx=10, pady=10, row=5, column=1)
        self.cancelbtn = tk.Button(self.master, text="Cancel", width=15, command=self.exit)
        self.cancelbtn.grid(sticky='W', padx=10, pady=10, row=5, column=2)

    def exit(self):
        self.master.destroy()

    def nirbandorderchanged(self, selectednirbandvalue):
        print selectednirbandvalue
        self.nirbandordervar = selectednirbandvalue;

    def swirbandorderchanged(self, selectedswirbandvalue):
        print selectedswirbandvalue
        self.swirbandordervar = selectedswirbandvalue

    def selectinputdatadir(self):
        self.inputdatadirpath = tkFileDialog.askdirectory(initialdir="/", title="Select Input Data Directory")
        self.inputdatadirfield.delete(1.0, tk.END)
        self.inputdatadirfield.insert(tk.END, self.inputdatadirpath)

    def selectoutputndwidir(self):
        self.outputndwidirpath = tkFileDialog.askdirectory(initialdir="/", title="Select Output NDWI Directory")
        self.outputndwidirfield.delete(1.0, tk.END)
        self.outputndwidirfield.insert(tk.END, self.outputndwidirpath)

    def computendwi(self):
        enteredinputdatadirpath = self.inputdatadirfield.get("1.0", tk.END)
        if(enteredinputdatadirpath.endswith("\n")):
            enteredinputdatadirpath = enteredinputdatadirpath[:-1]
        print enteredinputdatadirpath

        enteredoutputndwidirpath = self.outputndwidirfield.get("1.0", tk.END)
        if (enteredoutputndwidirpath.endswith("\n")):
            enteredoutputndwidirpath = enteredoutputndwidirpath[:-1]
        print enteredoutputndwidirpath

        enterednirbandorder = self.nirbandordervar
        print enterednirbandorder
        enteredswirbandorder =  self.swirbandordervar
        print enteredswirbandorder
        threshold = 0.5

        ndwi_tiff_modis.compute_ndwi(enteredinputdatadirpath, enteredoutputndwidirpath, enterednirbandorder, enteredswirbandorder, threshold)
