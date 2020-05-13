import tkFileDialog
import Tkinter as tk


class MOSAICClippingFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        # window title in the title bar
        self.master.title("MOSAIC Clipping and Computing Area and Volume of the Lakes")

        # window title label
        windowlbl = tk.Label(self.master, text="MOSAIC Clipping and Computing Area and Volume of the Lakes")
        windowlbl.grid(padx=10, pady=10, row=0, column=0, columnspan=4)

        # Input MOSAIC Data Directory
        inputmosaicdatadirlbl = tk.Label(self.master, text="Input MOSAIC Data Directory")
        inputmosaicdatadirlbl.grid(sticky='W', padx=10, pady=10, row=1, column=0)
        self.inputmosaicdatadirfield = tk.Text(self.master, height=1, width=45)
        self.inputmosaicdatadirfield.grid(sticky='W', padx=10, pady=10, row=1, column=1, columnspan=2)
        inputmosaicdatadirbtn = tk.Button(self.master, text="Browse", command=self.selectinputmosaicdatadir)
        inputmosaicdatadirbtn.grid(sticky='W', padx=10, pady=10, row=1, column=3)

        # Input Lakes Basins Directory
        inputlakesbasinsdirlbl = tk.Label(self.master, text="Input Lakes Basins Directory")
        inputlakesbasinsdirlbl.grid(sticky='W', padx=10, pady=10, row=2, column=0)
        self.inputlakesbasinsdirfield = tk.Text(self.master, height=1, width=45)
        self.inputlakesbasinsdirfield.grid(sticky='W', padx=10, pady=10, row=2, column=1, columnspan=2)
        inputlakesbasinsdirbtn = tk.Button(self.master, text="Browse", command=self.selectinputlakesbasinsdir)
        inputlakesbasinsdirbtn.grid(sticky='W', padx=10, pady=10, row=2, column=3)

        # Input Area/Volume Relation Table
        inputareavolumerelationtablelbl = tk.Label(self.master, text="Input Area/Volume Relation Table")
        inputareavolumerelationtablelbl.grid(sticky='W', padx=10, pady=10, row=3, column=0)
        self.inputareavolumerelationtablefield = tk.Text(self.master, height=1, width=45)
        self.inputareavolumerelationtablefield.grid(sticky='W', padx=10, pady=10, row=3, column=1, columnspan=2)
        inputareavolumerelationtablebtn = tk.Button(self.master, text="Browse",
                                                    command=self.selectinputareavolumerelationtable)
        inputareavolumerelationtablebtn.grid(sticky='W', padx=10, pady=10, row=3, column=3)

        # Output Lakes Area Table
        outputlakesareatablelbl = tk.Label(self.master, text="Output Lakes Area Table")
        outputlakesareatablelbl.grid(sticky='W', padx=10, pady=10, row=4, column=0)
        self.outputlakesareatablefield = tk.Text(self.master, height=1, width=45)
        self.outputlakesareatablefield.grid(sticky='W', padx=10, pady=10, row=4, column=1, columnspan=2)
        outputlakesareatablebtn = tk.Button(self.master, text="Browse", command=self.selectoutputlakesareatable)
        outputlakesareatablebtn.grid(sticky='W', padx=10, pady=10, row=4, column=3)

        # Output Lakes Volume Table
        outputlakesvolumetablelbl = tk.Label(self.master, text="Output Lakes Volume Table")
        outputlakesvolumetablelbl.grid(sticky='W', padx=10, pady=10, row=5, column=0)
        self.outputlakesvolumetablefield = tk.Text(self.master, height=1, width=45)
        self.outputlakesvolumetablefield.grid(sticky='W', padx=10, pady=10, row=5, column=1, columnspan=2)
        outputlakesvolumetabletablebtn = tk.Button(self.master, text="Browse",
                                                   command=self.selectoutputlakesvolumetable)
        outputlakesvolumetabletablebtn.grid(sticky='W', padx=10, pady=10, row=5, column=3)

        # control buttons
        self.startclippingprocessbtn = tk.Button(self.master, text="Start", width=15, command=self.startclippingprocess)
        self.startclippingprocessbtn.grid(sticky='E', padx=10, pady=10, row=6, column=1)
        self.cancelbtn = tk.Button(self.master, text="Cancel", width=15, command=self.exit)
        self.cancelbtn.grid(sticky='W', padx=10, pady=10, row=6, column=2)

    def exit(self):
        self.master.destroy()

    def selectinputmosaicdatadir(self):
        self.inputmosaicdatadirpath = tkFileDialog.askdirectory(initialdir="/", title="Select Input MOSAIC Data Directory")
        self.inputmosaicdatadirfield.delete(1.0, tk.END)
        self.inputmosaicdatadirfield.insert(tk.END, self.inputmosaicdatadirpath)

    def selectinputlakesbasinsdir(self):
        self.inputlakesbasinsdirpath = tkFileDialog.askdirectory(initialdir="/",
                                                                 title="Select Input Lakes Basins Directory")
        self.inputlakesbasinsdirfield.delete(1.0, tk.END)
        self.inputlakesbasinsdirfield.insert(tk.END, self.inputlakesbasinsdirpath)

    def selectinputareavolumerelationtable(self):
        self.inputareavolumerelationtablepath = tkFileDialog.askopenfilename(initialdir="/",
                                                           title="Select Input Area/Volume Relation Table",
                                                           filetypes=(
                                                               ("Excel Sheet", "*.xlsx"), ("All Files", "*.*")))
        self.inputareavolumerelationtablefield.delete(1.0, tk.END)
        self.inputareavolumerelationtablefield.insert(tk.END, self.inputareavolumerelationtablepath)

    def selectoutputlakesareatable(self):
        self.outputlakesareatablepath = tkFileDialog.asksaveasfilename(initialdir="/",
                                                                    title="Select Output Lakes Area Table",
                                                                    filetypes=(
                                                                        ("Excel Sheet", "*.xlsx"),
                                                                        ("All Files", "*.*")))
        self.outputlakesareatablefield.delete(1.0, tk.END)
        self.outputlakesareatablefield.insert(tk.END, self.outputlakesareatablepath)

    def selectoutputlakesvolumetable(self):
        self.outputlakesvolumetablepath = tkFileDialog.asksaveasfilename(initialdir="/",
                                                                    title="Select Output Lakes Volume Table",
                                                                    filetypes=(
                                                                        ("Excel Sheet", "*.xlsx"),
                                                                        ("All Files", "*.*")))
        self.outputlakesvolumetablefield.delete(1.0, tk.END)
        self.outputlakesvolumetablefield.insert(tk.END, self.outputlakesvolumetablepath)

    def startclippingprocess(self):
        enteredinputmosaicdatadirpath = self.inputmosaicdatadirfield.get("1.0", tk.END)
        print enteredinputmosaicdatadirpath
        enteredinputlakesbasinsdirpath = self.inputlakesbasinsdirfield.get("1.0", tk.END)
        print enteredinputlakesbasinsdirpath
        enteredinputareavolumerelationtablepath = self.inputareavolumerelationtablefield.get("1.0", tk.END)
        print enteredinputareavolumerelationtablepath
        enteredoutputlakesareatablepath = self.outputlakesareatablefield.get("1.0", tk.END)
        print enteredoutputlakesareatablepath
        enteredoutputlakesvolumetablepath = self.outputlakesvolumetablefield.get("1.0", tk.END)
        print enteredoutputlakesvolumetablepath
