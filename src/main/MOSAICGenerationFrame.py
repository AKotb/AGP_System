import tkFileDialog
import Tkinter as tk
import ndwi_mosaic

class MOSAICGenerationFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # window title in the title bar
        self.master.title("NDWI MOSAIC Generation")

        # window title label
        windowlbl = tk.Label(self.master, text="NDWI MOSAIC Generation")
        windowlbl.grid(padx=10, pady=10, row=0, column=0, columnspan=4)

        # Enter Input NDWI Data Directory
        inputndwidatadirlbl = tk.Label(self.master, text="Input NDWI Data Directory")
        inputndwidatadirlbl.grid(sticky='W', padx=10, pady=10, row=1, column=0)
        self.inputndwidatadirfield = tk.Text(self.master, height=1, width=45)
        self.inputndwidatadirfield.grid(sticky='W', padx=10, pady=10, row=1, column=1, columnspan=2)
        inputndwidatadirbtn = tk.Button(self.master, text="Browse", command=self.selectinputndwidatadir)
        inputndwidatadirbtn.grid(sticky='W', padx=10, pady=10, row=1, column=3)

        # Output NDWI MOSAIC Directory
        outputndwimosaicdirlbl = tk.Label(self.master, text="Output NDWI MOSAIC Directory")
        outputndwimosaicdirlbl.grid(sticky='W', padx=10, pady=10, row=2, column=0)
        self.outputndwimosaicdirfield = tk.Text(self.master, height=1, width=45)
        self.outputndwimosaicdirfield.grid(sticky='W', padx=10, pady=10, row=2, column=1, columnspan=2)
        outputndwimosaicdirbtn = tk.Button(self.master, text="Browse", command=self.selectoutputndwimosaicdir)
        outputndwimosaicdirbtn.grid(sticky='W', padx=10, pady=10, row=2, column=3)

        # control buttons
        self.startgeneratingndwimosaicbtn = tk.Button(self.master, text="Generate", width=15, command=self.generatendwimosaic)
        self.startgeneratingndwimosaicbtn.grid(sticky='E', padx=10, pady=10, row=3, column=1)
        self.cancelbtn = tk.Button(self.master, text="Cancel", width=15, command=self.exit)
        self.cancelbtn.grid(sticky='W', padx=10, pady=10, row=3, column=2)

    def exit(self):
        self.master.destroy()

    def selectinputndwidatadir(self):
        self.inputndwidatadirpath = tkFileDialog.askdirectory(initialdir="/", title="Select Input NDWI Data Directory")
        self.inputndwidatadirfield.delete(1.0, tk.END)
        self.inputndwidatadirfield.insert(tk.END, self.inputndwidatadirpath)

    def selectoutputndwimosaicdir(self):
        self.outputndwimosaicdirpath = tkFileDialog.askdirectory(initialdir="/", title="Select Output NDWI MOSAIC Directory")
        self.outputndwimosaicdirfield.delete(1.0, tk.END)
        self.outputndwimosaicdirfield.insert(tk.END, self.outputndwimosaicdirpath)

    def generatendwimosaic(self):
        enteredinputndwidatadirpath = self.inputndwidatadirfield.get("1.0", tk.END)
        if (enteredinputndwidatadirpath.endswith("\n")):
            enteredinputndwidatadirpath = enteredinputndwidatadirpath[:-1]
        print enteredinputndwidatadirpath

        enteredoutputndwimosaicdirpath = self.outputndwimosaicdirfield.get("1.0", tk.END)
        if (enteredoutputndwimosaicdirpath.endswith("\n")):
            enteredoutputndwimosaicdirpath = enteredoutputndwimosaicdirpath[:-1]
        print enteredoutputndwimosaicdirpath

        ndwi_mosaic.generate_ndwi_mosaic_batch(enteredinputndwidatadirpath, enteredoutputndwimosaicdirpath)