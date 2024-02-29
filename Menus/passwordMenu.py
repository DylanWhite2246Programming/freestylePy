#import time
#import board
#import busio
#from digitalio import DigitalInOut, Direction
#import adafruit_fingerprint

import tkinter as tk
from tkinter import messagebox
import csv
from assets.constants import MENU_BG_COLOR, BUTTON_BG_COLOR, BUTTON_FG_COLOR, RESOLUTION, USERS_CSV_PATH
from Menus.mainMenu import mainMenu

class PasswordMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.menu_bg_color = MENU_BG_COLOR
        self.button_bg_color = BUTTON_BG_COLOR
        self.button_fg_color = BUTTON_FG_COLOR

        self.password_window = tk.Toplevel(self.root)
        self.password_window.title("Password")
        self.password_window.geometry(RESOLUTION)
        self.password_window.configure(bg=self.menu_bg_color)

        self.password_entry = tk.Entry(self.password_window, show='*')
        self.password_entry.grid(columnspan=3, padx=5, pady=5)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            'Clear', '0', 'Enter'
        ]

        for i, button in enumerate(buttons):
            row = i // 3 + 1
            col = (i % 3)
            if button == 'Clear':
                tk.Button(self.password_window, text=button, command=self.clear_password, bg=self.button_bg_color,
                          fg=self.button_fg_color, width=10, height=6).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'Enter':
                #tk.Button(self.password_window, text=button, command=self.open_main_menu, bg=self.button_bg_color,
                tk.Button(self.password_window, text=button, bg=self.button_bg_color,
                          fg=self.button_fg_color, widt=10, height=6).grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(self.password_window, text=button, command=lambda b=button: self.enter_digit(b),
                          bg=self.button_bg_color, fg=self.button_fg_color, width=10, height=6).grid(row=row,
                                                                                                         column=col,
                                                                                                         padx=5,
                                                                                                         pady=5)

        self.root.mainloop()

    def authenticate_password(self):
        entered_password = self.password_entry.get()
        with open(USERS_CSV_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == entered_password:
                    return True, row[1], row[2]
        return False, None, None

    def enter_digit(self, digit):
        current_password = self.password_entry.get()
        current_password += str(digit)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, current_password)

    def clear_password(self):
        self.password_entry.delete(0, tk.END)

    def open_main_menu(self):
        authenticated, name, balance = self.authenticate_password()
        if authenticated:
            self.root.withdraw()
            self.password_window.withdraw()
            main_menu = mainMenu(name)
        else:
            messagebox.showerror("Error", "Invalid password!")
