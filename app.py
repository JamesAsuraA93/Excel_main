import tkinter as tk
from tkinter import ttk
from main import main_process


class Generator_card_Shuffle(ttk.Frame):
    # default
    number_of_rows = 20
    value = 'เทส'
    position = 4
    file_name = 'A'

    def __init__(self, master=None):
        super().__init__(master)
        self.title = "Generator Card Shuffle Ver.1.1"
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        number_of_rows = tk.StringVar()
        file_name = tk.StringVar()

        # Entry rows
        self.label_number = ttk.Label(self, text="Number of rows")
        self.input_number = ttk.Entry(self, textvariable=number_of_rows)

        # Entry file_name
        self.label_name = ttk.Label(self, text="File name")
        self.input_name = ttk.Entry(self, textvariable=file_name)

        # option menu
        option_list = ('เทส', 'ไฟล์จริง')
        self.option_menu = ttk
        value = tk.StringVar(self)
        value.set('เลือก Option')
        self.option_menu = tk.OptionMenu(self, value, *option_list)
        self.option_menu.config(width=10)

        # start_with
        start_with = ('4', '5', '6', '7', '8', '9', '10', '11')
        self.start_with_menu = ttk
        value2 = tk.StringVar(self)
        value2.set('เลือกตำแหน่งให้การ์ดก่อน')
        self.start_with_menu = tk.OptionMenu(self, value2, *start_with)
        self.start_with_menu.config(width=15)

        # button shuffle
        self.button_shuffle = ttk.Button(self, text="Shuffle", command=self.shuffle)

        self.label_number.grid(row=1, column=1, columnspan=4, pady=5, sticky="N")
        self.input_number.grid(row=2, column=1, columnspan=3, pady=5, sticky="N")
        self.label_name.grid(row=3, column=1, columnspan=4, pady=5, sticky="N")
        self.input_name.grid(row=4, column=1, columnspan=3, pady=5, sticky="N")
        self.option_menu.grid(row=5, column=1, columnspan=3, pady=10, sticky="N")
        self.start_with_menu.grid(row=6, column=1, columnspan=3, pady=10, sticky="N")
        self.button_shuffle.grid(row=7, column=1, columnspan=3, pady=10, sticky="N")

        self.number_of_rows = number_of_rows
        self.value = value
        self.file_name = file_name
        self.position = value2

    def shuffle(self):
        # pop up window confirm
        self.popup_confirm = tk.Tk()
        self.popup_confirm.title("Confirm")
        self.popup_confirm.geometry("200x100")
        # show label __number_of_rows Middle of the screen
        if self.number_of_rows.get():
            self.label_confirm = ttk.Label(self.popup_confirm,text="Number of cards: " + self.number_of_rows.get())
        else:
            self.label_confirm = ttk.Label(self.popup_confirm, text="Number of cards: " + '0')
        self.label_confirm.grid(row=1, column=1, columnspan=2, padx=40, pady=10, sticky="NE")

        self.button_confirm = ttk.Button(self.popup_confirm, text="Confirm", command=self.confirm)

        self.button_confirm.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.popup_confirm.resizable(False, False)

    def confirm(self):
        self.popup_confirm.destroy()
        if self.get_option() == 'ไฟล์จริง':

            main_process(self.get_file_name(),int(self.get_number_of_rows()), int(self.get_position()),1)
        elif self.get_option() == 'เทส':
            main_process(self.get_file_name(),int(self.get_number_of_rows()), int(self.get_position()),0)

    def get_number_of_rows(self):
        return self.number_of_rows.get()

    def get_option(self):
        return self.value.get()

    def get_position(self):
        return self.position.get()

    def get_file_name(self):
        return self.file_name.get()


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Generator Card Shuffle")
    app.geometry("350x300")
    app = Generator_card_Shuffle(master=app)
    app.mainloop()
