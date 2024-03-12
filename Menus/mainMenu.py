import tkinter as tk
from assets import constants
from Menus.drinkMenu import drinkMenu
import math

def mainMenu(name,balance,admin):
    #first row


    window = tk.Tk()
    window.geometry(constants.RESOLUTION)
    window.configure(bg=constants.MENU_BG_COLOR)

    def logout_button_pressed():
        window.destroy()

    topbar = tk.Frame(window, width=480, bg=constants.MENU_BG_COLOR)
    topbar.grid(row=0,column=0,columnspan=5)

    name_var = tk.StringVar(value=name)
    balance_var = tk.StringVar(value='$'+str(balance))

    name_label = tk.Label(topbar, text='Name: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR , width=10)
    name_label.grid(row=0, column=0, padx=5,sticky='e')
    name_entry = tk.Entry(topbar, textvariable=name_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR,width=10)
    name_entry.grid(row=0, column=1, padx=5,sticky='w')

    balance_label = tk.Label(topbar, text='Balance: ',bg=constants.MENU_BG_COLOR,fg=constants.BUTTON_BG_COLOR, width=10)
    balance_label.grid(row=0, column=2, padx=5,sticky='e')
    balance_entry = tk.Entry(topbar, textvariable=balance_var, state='readonly',readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR, width=10)
    balance_entry.grid(row=0, column=3, padx=5,sticky='w')

    if admin:
        adjustBalance_Button = tk.Button(topbar, text='Adjust Balance', bg=constants.BUTTON_BG_COLOR, fg=constants.BUTTON_FG_COLOR, width=13)
        adjustBalance_Button.grid(row=0,column=4,padx=5)

        appendUser_button = tk.Button(topbar, text='Add New User', bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR, width=13)
        appendUser_button.grid(row=0,column=5,padx=5)

    logout_button = tk.Button(topbar, text='Logout',command=logout_button_pressed,bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR, width=10)
    logout_button.grid(row=0, column=6, padx=5)

    #second row and beyond

    drinks = ["SOTB", "Vodka Cran", "Screw Driver", "Jungle Juice", "Negroni", 
              "Cosmo", "Margarita", "Cum and Roke","Green Tea", "test"]
    
    for i, drink in enumerate(drinks):
        button = tk.Button(window, text=drink, command=lambda drink=drink: drinkMenu(window, drink, name, balance),bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR, height=2, width=20)
        button.grid(row=math.floor(i/5)+1,column=i%5, sticky='ew', padx=5, pady=5)
        #window.grid_columnconfigure(i%5,weight=0)

    window.grid_rowconfigure(0,weight=0)

    window.mainloop()
