from tkinter import *
from tkinter import messagebox

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

        # Drop down menu
        self.first_choice = DropDownMenu(window, 2, 0, 1) 

        to_temperature_label = Label(window, text="To", font=("Arial", 14, "normal"))
        to_temperature_label.grid(sticky="w", row=1, column=1)

        self.second_choice = DropDownMenu(window, 2, 1, 2)

        # Input entry and button

        input_value = Entry()
        input_value.grid(sticky="w", row=4, column=0, pady=35)
        input_value.insert(END, "Input the value here...")

        button = Button(text="Convert", command=self.show_value, width=10)
        button.grid(sticky="w", row=5, column=0)

        window.mainloop()
        
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