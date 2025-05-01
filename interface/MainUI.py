from tkinter import *

class TemperatureConverterInterface:

    def __init__(self):
        window = Tk()
        window.title("Temperature Converter")
        window.minsize(width=640, height=350)
        window.config(padx=20, pady=20)

        # Labels
        app_label = Label(window, text="Convert Temperature", font=("Times New Roman", 24, "bold"))
        app_label.grid(sticky="w", row=0, column=0)
        app_label.config(pady=10, padx=10)

        from_temperature_label = Label(window, text="From", font=("Arial", 14, "normal"))
        from_temperature_label.grid(sticky="w", row=1, column=0)

        to_temperature_label = Label(window, text="To", font=("Arial", 14, "normal"))
        to_temperature_label.grid(sticky="w", row=1, column=1)

        window.mainloop()
