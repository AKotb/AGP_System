import tkMessageBox
import LSMProcessing
import MonthIndexFrame
import NCtoTiff
import TWSMassAnomaliesCalculator
import TWStoTiff
import TemporalMeanFrame
import Tkinter as tk
import ZonalStatistics
import DataSubsetFrame
import NDWIComputationFrame
import MOSAICGenerationFrame
import MOSAICClippingFrame
import GWSComputation


class HomeWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()
 
    def init_window(self):
        self.master.title("AGPS Home")
        self.pack(fill=tk.BOTH, expand=1)

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        # File Menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)

        # Processing Menu
        processingmenu = tk.Menu(menubar, tearoff=0)
        processingmenu.add_command(label="Month Index", command=self.monthindex)
        processingmenu.add_command(label="Temporal Mean", command=self.temporalmean)
        processingmenu.add_command(label="Calculate TWS Mass Anomalies", command=self.twsmassanomalies)
        processingmenu.add_command(label="TWS Mass to GeoTiff", command=self.createtiff)
        
        processingmenu.add_separator()
        processingmenu.add_command(label="NC to GeoTiff", command=self.nctogeotiff)
        
        processingmenu.add_separator()
        processingmenu.add_command(label="LSM Processing", command=self.processlsm)
        
        processingmenu.add_separator()
        processingmenu.add_command(label="Zonal Statistics", command=self.zonalstatistics)
        menubar.add_cascade(label="Processing", menu=processingmenu)
        
        lakesmenu = tk.Menu(menubar, tearoff=0)
        # lakesmenu.add_command(label="Subset Data", command=self.subset_data)
        lakesmenu.add_command(label="Compute NDWI", command=self.compute_ndwi)
        lakesmenu.add_command(label="Generate MOSAIC", command=self.generate_mosaic)
        lakesmenu.add_command(label="Clip MOSAIC", command=self.clip_mosaic)
        menubar.add_cascade(label="Lakes Processing", menu=lakesmenu)

        gwsmenu = tk.Menu(menubar, tearoff=0)
        gwsmenu.add_command(label="Ground Water Storage", command=self.compute_gws)
        menubar.add_cascade(label="Ground Water", menu=gwsmenu)

        trmmmenu = tk.Menu(menubar, tearoff=0)
        trmmmenu.add_command(label="NC to GeoTIFF", command=self.nctogeotiff)
        trmmmenu.add_command(label="Zonal Statistics", command=self.zonalstatistics)
        menubar.add_cascade(label="TRMM", menu=trmmmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=helpmenu)

    def exit(self):
        exit()

    def open(self):
        print ("Open Menu Item Pressed!")

    def about(self):
        tkMessageBox.showinfo("AGPS",
                              "Automated GRACE Processing System."
                              "AGPS Version 0.1")

    def monthindex(self):
        root = tk.Tk()
        root.geometry("600x250")
        MonthIndexFrame.MonthIndexFrame(root)
        root.mainloop()

    def temporalmean(self):
        root = tk.Tk()
        root.geometry("600x250")
        TemporalMeanFrame.TemporalMeanFrame(root)
        root.mainloop()

    def twsmassanomalies(self):
        root = tk.Tk()
        root.geometry("600x300")
        TWSMassAnomaliesCalculator.TWSMassAnomaliesCalculator(root)
        root.mainloop()

    def createtiff(self):
        root = tk.Tk()
        root.geometry("600x250")
        TWStoTiff.TWStoTiff(root)
        root.mainloop()
        
    def nctogeotiff(self):
        root = tk.Tk()
        root.geometry("600x300")
        NCtoTiff.NCtoTiff(root)
        root.mainloop()
        
    def processlsm(self):
        root = tk.Tk()
        root.geometry("650x350")
        LSMProcessing.LSMProcessing(root)
        root.mainloop()

    def zonalstatistics(self):
        root = tk.Tk()
        root.geometry("650x250")
        ZonalStatistics.ZonalStatistics(root)
        root.mainloop() 
        
    """def subset_data(self):
        root = tk.Tk()
        root.geometry("600x300")
        DataSubsetFrame.DataSubsetFrame(root)
        root.mainloop()"""
        
    def compute_ndwi(self):
        root = tk.Tk()
        root.geometry("650x350")
        NDWIComputationFrame.NDWIComputationFrame(root)
        root.mainloop()
        
    def generate_mosaic(self):
        root = tk.Tk()
        root.geometry("700x250")
        MOSAICGenerationFrame.MOSAICGenerationFrame(root)
        root.mainloop()
        
    def clip_mosaic(self):
        root = tk.Tk()
        root.geometry("700x350")
        MOSAICClippingFrame.MOSAICClippingFrame(root)
        root.mainloop()

    def compute_gws(self):
        root = tk.Tk()
        root.geometry("650x400")
        GWSComputation.GWSComputation(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x20+50+50")
    root.overrideredirect(0)
    root.config(bg="blue")
    app = HomeWindow(root)
    root.mainloop()
