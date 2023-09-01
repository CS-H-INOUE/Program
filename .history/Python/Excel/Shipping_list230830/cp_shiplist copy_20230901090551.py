import os
import openpyxl
import xlwings as xw
from datetime import datetime, timedelta
import time
from tqdm import tqdm
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Days")
        self.selected_days = []

        self.current_day = tk.IntVar()
        self.current_day.set(datetime.now().day)

        self.label = ttk.Label(root, text="Select starting day:")
        self.label.pack(padx=10, pady=5)

        self.day_combobox = ttk.Combobox(root, textvariable=self.current_day, values=self.get_selectable_days())
        self.day_combobox.pack(padx=10, pady=5)

        self.confirm_button = ttk.Button(root, text="Confirm", command=self.confirm_selection)
        self.confirm_button.pack(padx=10, pady=10)

        # Bind the close event to a function
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def get_selectable_days(self):
        today = datetime.now().day
        current_month = datetime.now().month
        current_year = datetime.now().year
        last_day_of_month = (datetime(current_year, current_month + 1, 1) - timedelta(days=1)).day
        selectable_days = [(today + i) % last_day_of_month for i in range(3)]
        return [f"{current_month}/{day}/{current_year}" for day in selectable_days]

    def confirm_selection(self):
        today = datetime.now().day
        start_day = self.current_day.get()
        self.selected_days = [(start_day + i) % 30 for i in range(3) if (start_day + i) % 30 >= today]
        self.root.destroy()

    def close_app(self):
        self.root.destroy()





# Logic: Check if date matches selected days
def date_matches_selected_days(date_str, selected_days):
    try:
        day = map(int, date_str.split('/'))
        return day in selected_days
    except:
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    main(app.selected_days)
