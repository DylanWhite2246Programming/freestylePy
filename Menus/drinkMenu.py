import tkinter as tk
from assets import constants

def drinkMenu(mainMenu, drink, name, balance):
    thiswindow = tk.Toplevel(mainMenu)
    thiswindow.geometry(constants.RESOLUTION)
    thiswindow.configure(bg=constants.MENU_BG_COLOR)

    name_var = tk.StringVar(value=name)
    balance_var = tk.StringVar(value='$'+str(balance))
    drink_var = tk.StringVar(value=drink)
    percentage_var = tk.StringVar(value='0%')
    price_var = tk.StringVar(value='$0')

    name_label = tk.Label(thiswindow, text='Name: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    name_label.grid(row=0, column=0, padx=5,sticky='e')
    name_entry = tk.Entry(thiswindow, textvariable=name_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    name_entry.grid(row=0, column=1, padx=5,sticky='w')

    balance_label = tk.Label(thiswindow, text='Balance: ',bg=constants.MENU_BG_COLOR,fg=constants.BUTTON_BG_COLOR)
    balance_label.grid(row=0,column=2, padx=5,sticky='e')
    balance_entry = tk.Entry(thiswindow, textvariable=balance_var, state='readonly',readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    balance_entry.grid(row=0, column=3, padx=5,sticky='w')

    back_button = tk.Button(thiswindow, text='Back', bg=constants.BUTTON_BG_COLOR, fg=constants.BUTTON_FG_COLOR, command=thiswindow.destroy)
    back_button.grid(row=0, column=4, padx=4)
    logout_button = tk.Button(thiswindow, text='Logout',bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR)
    logout_button.grid(row=0, column=5, padx=5)

    drink_label = tk.Label(thiswindow, text='Drink: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    drink_label.grid(row=1,column=0,padx=5,sticky='w')
    drink_entry = tk.Entry(thiswindow, textvariable=drink_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    drink_entry.grid(row=1,column=1,padx=5,sticky='e')
    percentage_label = tk.Label(thiswindow, text='Percentage: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    percentage_label.grid(row=1,column=2,sticky='w')
    percentage_

    thiswindow.grid_columnconfigure((0,1,2,3,4,5),weight=1)
    thiswindow.grid_rowconfigure(0,weight=0)

    thiswindow.mainloop()

