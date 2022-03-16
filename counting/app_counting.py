import tkinter as tk
from tkinter import ttk
from process import main

class Generator_card_Shuffle(ttk.Frame):
    # default
    name_file_to_count = 'A'

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        file_to_count = tk.StringVar()

        self.label_file_to_count = ttk.Label(self, text='Counting Flop Pattern')
        self.label_file_to_count.grid(row=0, column=0, columnspan=4, sticky='N',pady=15)
        self.label_name_file_to_count = ttk.Label(self, text="Name file to count:")
        self.label_name_file_to_count.grid(row=1, column=0, sticky=tk.W)
        self.entry_number_of_rows = ttk.Entry(self, width=10, textvariable=file_to_count)
        self.entry_number_of_rows.grid(row=1, column=1, sticky=tk.W, padx=5)

        self.button_counting = ttk.Button(self, text="Shuffle", command=self.counting)
        self.button_counting.grid(row=3, column=0, columnspan=4, pady=20, sticky="N")

        self.name_file_to_count = file_to_count.get()

    def counting(self):
        self.name_file_to_count = self.entry_number_of_rows.get()
        main(self.name_file_to_count)
        self.popup()

    def popup(self):
        self.popup_window = tk.Toplevel()
        self.popup_window.title("Done!")
        self.popup_window.geometry("150x50")
        self.popup_window.resizable(False, False)
        self.popup_window.wm_attributes("-topmost", 1)
        self.button_counting = ttk.Button(self.popup_window, text="OK", command=self.popup_window.destroy)
        self.button_counting.grid(row=3, column=0, columnspan=4, pady=20, sticky="N")
        self.button_counting.pack()




if __name__ == "__main__":
    app = tk.Tk()
    app.title("Flop Counting")
    app.geometry("250x170")
    app = Generator_card_Shuffle(master=app)
    app.mainloop()
