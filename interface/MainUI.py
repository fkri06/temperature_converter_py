from tkinter import *
from tkinter import messagebox
from enum import Enum
from converter.converter import *

class Temp(Enum):
    CELCIUS     = 1
    FAHRENHEIT  = 2
    KELVIN      = 3

class TemperatureConverterInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Temperature Converter")
        self.window.minsize(width=640, height=350)
        self.window.config(padx=20, pady=20)
        
        # Labels
        self.app_label = Label(self.window, text="Convert Temperature", font=("Times New Roman", 24, "bold"))
        self.app_label.grid(sticky="w", row=0, column=0)
        self.app_label.config(pady=10, padx=10)

        self.from_temperature_label = Label(self.window, text="From", font=("Arial", 14, "normal"))
        self.from_temperature_label.grid(sticky="w", row=1, column=0)

        # Drop down menu
        self.first_choice = DropDownMenu(self.window, 2, 0, 1) 

        self.to_temperature_label = Label(self.window, text="To", font=("Arial", 14, "normal"))
        self.to_temperature_label.grid(sticky="w", row=1, column=1)

        self.second_choice = DropDownMenu(self.window, 2, 1, 2)

        # Input entry and button
        self.input_value = Entry()
        self.input_value.grid(sticky="w", row=4, column=0, pady=35)

        self.button = Button(text="Convert", command=self.calculate, width=10, font=("Arial", 12, "bold"), fg="#36454F")
        self.button.grid(sticky="w", row=5, column=0)


        # Label to show the converted value
        self.show_converted_value = Label(text="Text", font=("Arial", 24, "bold"))
        self.show_converted_value.grid(sticky="w", row=4, column=1)


        self.window.mainloop()
    
    def calculate(self):
        pass
        
class DropDownMenu:
    def __init__(self, window: Tk, row: int, column: int, rowspan: int):
        self.options = ["Celcius", "Fahrenheit", "Kelvin"]
        self.selected_option = StringVar(window)
        self.selected_option.set("Choose temperature")
        self.drop_down = OptionMenu(window, self.selected_option, *self.options, command=self.set_menu_value)
        self.value = ""
        self.drop_down.grid(sticky="w", row=row, column=column, rowspan=rowspan)
    
    def set_menu_value(self, value):
        self.value = value