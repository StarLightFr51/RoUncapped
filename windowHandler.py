import tkinter as tk
import assetsHandler

class window:
    win = tk.Tk()

    def loop(self, title, geometry):
        self.win.title(title)
        self.win.geometry(geometry)
        self.win.resizable(False, False)

        assetsHandler.assets.add_label(assetsHandler.assets(), self.win, "Enter the amount of fps you want then press the Enter Key : ", "", 10, "")
        assetsHandler.assets.add_entry(assetsHandler.assets(), self.win)
        self.win.mainloop()
