from tkinter import *

class TemperatureConverterInterface:

    def __init__(self):
        window = Tk()
        window.title("Temperature Converter")
        window.minsize(width=500, height=500)
        window.config(padx=20, pady=20)
        window.mainloop()
