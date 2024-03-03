import tkinter as tk
from assets import constants
from Menus.drinkMenu import drinkMenu

def mainMenu(name,balance,admin):
    window = tk.Tk()
    window.geometry(constants.RESOLUTION)
    window.configure(bg=constants.MENU_BG_COLOR)

    name_var = tk.StringVar(value=name)
    balance_var = tk.StringVar(value='$'+str(balance))

    name_label = tk.Label(window, text='Name: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    name_label.grid(row=0, column=0, padx=5,sticky='e')
    name_entry = tk.Entry(window, textvariable=name_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    name_entry.grid(row=0, column=1, padx=5,sticky='w')

    balance_label = tk.Label(window, text='Balance: ',bg=constants.MENU_BG_COLOR,fg=constants.BUTTON_BG_COLOR)
    balance_label.grid(row=0,column=2, padx=5,sticky='e')
    balance_entry = tk.Entry(window, textvariable=balance_var, state='readonly',readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    balance_entry.grid(row=0, column=3, padx=5,sticky='w')

    if admin:
        appendUser_button = tk.Button(window, text='Add New User', bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR)
        appendUser_button.grid(row=0,column=4,padx=5)

    logout_button = tk.Button(window, text='Logout',bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR)
    logout_button.grid(row=0, column=5, padx=5)

    drinks = ["SOTB", "Vodka Cran", "Screw Driver", "Jungle Juice",
                "Negroni", "Cosmo", "Margarita", "Cum and Roke"]
    
    for i, drink in enumerate(drinks):
        button = tk.Button(window, text=drink, command=lambda drink=drink: drinkMenu(window, drink, name, balance),bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR, height=2, width=20)
        button.grid(row=i//4*2+1,column=i%4, sticky='ew', padx=5, pady=5)
        window.grid_columnconfigure(i%4,weight=0)

    window.grid_rowconfigure(0,weight=0)

    window.mainloop()
