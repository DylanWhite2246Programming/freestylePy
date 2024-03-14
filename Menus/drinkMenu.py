import tkinter as tk
from assets import constants
from assets import utilities

def drinkMenu(mainMenu, drink, name, balance):
    last_amount_button = None
    last_shot_button = None
    thiswindow = tk.Toplevel(mainMenu)
    thiswindow.geometry(constants.RESOLUTION)
    thiswindow.configure(bg=constants.MENU_BG_COLOR)

    name_var = tk.StringVar(value=name)
    balance_var = tk.StringVar(value='$'+str(balance))
    drink_var = tk.StringVar(value=drink)
    percentage_var = tk.StringVar(value='0%')
    price_var = tk.StringVar(value='$0')

    #row 0 and 1
    topbar = tk.Frame(thiswindow, width=480, bg=constants.MENU_BG_COLOR)
    topbar.grid(row=0,column=0,columnspan=5,rowspan=2)

    name_label = tk.Label(topbar, text='Name: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    name_label.grid(row=0, column=0, padx=5,sticky='e')
    name_entry = tk.Entry(topbar, textvariable=name_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    name_entry.grid(row=0, column=1, padx=5,sticky='w')

    balance_label = tk.Label(topbar, text='Balance: ',bg=constants.MENU_BG_COLOR,fg=constants.BUTTON_BG_COLOR)
    balance_label.grid(row=0,column=2, padx=5,sticky='e')
    balance_entry = tk.Entry(topbar, textvariable=balance_var, state='readonly',readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR,width=10)
    balance_entry.grid(row=0, column=3, padx=5,sticky='w')

    back_button = tk.Button(topbar, text='Back', bg=constants.BUTTON_BG_COLOR, fg=constants.BUTTON_FG_COLOR, command=thiswindow.destroy, width=10)
    back_button.grid(row=0, column=4, padx=4)
    logout_button = tk.Button(topbar, text='Logout',bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR , width=10)
    logout_button.grid(row=0, column=5, padx=5)

    drink_label = tk.Label(topbar, text='Drink: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    drink_label.grid(row=1,column=0,padx=5,sticky='e')
    drink_entry = tk.Entry(topbar, textvariable=drink_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    drink_entry.grid(row=1,column=1,padx=5,sticky='w')
    percentage_label = tk.Label(topbar, text='Percentage: ', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    percentage_label.grid(row=1,column=2,sticky='e')
    percentage_entry = tk.Entry(topbar, textvariable=percentage_var, state='readonly', readonlybackground=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR, width=10)
    percentage_entry.grid(row=1,column=3, sticky='w')
    price_label = tk.Label(topbar, text='Price: ', bg=constants.MENU_BG_COLOR,fg=constants.BUTTON_BG_COLOR)
    price_label.grid(row=1,column=4,sticky='e')
    price_entry = tk.Entry(topbar, textvariable=price_var, bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR, width=10)
    price_entry.grid(row=1,column=5,sticky='w')

    def amount_button_pressed(button):
        nonlocal last_amount_button
        if last_amount_button:
            last_amount_button.config(bg=constants.BUTTON_BG_COLOR, fg=constants.BUTTON_FG_COLOR)
        last_amount_button = button
        button.config(bg=constants.BUTTON_FG_COLOR,fg=constants.BUTTON_BG_COLOR)

        if last_shot_button:
            price = utilities.calculate_price(drink_entry.get(), int(last_shot_button['text']), float(last_amount_button['text']))
            percentage = utilities.calculate_percentage(drink_entry.get(), int(last_shot_button['text']), float(last_amount_button['text']))
            price_entry.config(state='normal')
            percentage_entry.config(state='normal')
            price_entry.delete(0,tk.END)
            price_entry.insert(0,'$'+str(price))
            percentage_entry.delete(0,tk.END)
            percentage_entry.insert(0,str(percentage)+'%')
            price_entry.config(state="readonly",readonlybackground=constants.MENU_BG_COLOR)
            percentage_entry.config(state="readonly",readonlybackground=constants.MENU_BG_COLOR)

    def shot_button_pressed(button):
        nonlocal last_shot_button
        if last_shot_button:
            last_shot_button.config(bg=constants.BUTTON_BG_COLOR, fg=constants.BUTTON_FG_COLOR)
        last_shot_button = button
        button.config(bg=constants.BUTTON_FG_COLOR,fg=constants.BUTTON_BG_COLOR)
        if last_amount_button:
            price = utilities.calculate_price(drink_entry.get(), int(last_shot_button['text']), float(last_amount_button['text']))
            percentage = utilities.calculate_percentage(drink_entry.get(), int(last_shot_button['text']), float(last_amount_button['text']))
            price_entry.config(state='normal')
            percentage_entry.config(state='normal')
            price_entry.delete(0,tk.END)
            price_entry.insert(0,'$'+str(price))
            percentage_entry.delete(0,tk.END)
            percentage_entry.insert(0,str(percentage)+'%')
            price_entry.config(state="readonly",readonlybackground=constants.MENU_BG_COLOR)
            percentage_entry.config(state="readonly",readonlybackground=constants.MENU_BG_COLOR)

    shot_label = tk.Label(thiswindow,text='Number Of Shots', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    shot_label.grid(row=2,column=0,sticky='e')
    amount_label = tk.Label(thiswindow, text='Amount (oz)', bg=constants.MENU_BG_COLOR, fg=constants.BUTTON_BG_COLOR)
    amount_label.grid(row=3,column=0,sticky='e')
    
    shotButtons=[]
    amountButtons=[]

    #row 2


    for i in range(0,5):
        shotButton = tk.Button(thiswindow,text=str(i+1),width=10, padx= 2,pady=2,bg=constants.BUTTON_BG_COLOR, fg=constants.BUTTON_FG_COLOR)
        shotButton.grid(row=2,column=i+1,pady=2)
        shotButton.config(command= lambda btn = shotButton : shot_button_pressed(btn))
        amountButton = tk.Button(thiswindow,text=2*i+8,width=10,padx=2,pady=2,bg=constants.BUTTON_BG_COLOR,fg=constants.BUTTON_FG_COLOR)
        amountButton.grid(row=3,column=i+1,pady=2)
        amountButton.config(command= lambda btn = amountButton : amount_button_pressed(btn))
        amountButtons.append(amountButton)
        shotButtons.append(shotButton)


    thiswindow.grid_columnconfigure((0,1,2,3,4,5),weight=0)
    thiswindow.grid_rowconfigure(0,weight=0)

    thiswindow.mainloop()

