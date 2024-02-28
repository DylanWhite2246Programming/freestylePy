import tkinter as tk
from tkinter import messagebox
import csv

# Set colors
menu_bg_color = "#79242F"  # RGB values R158 G137 B89
button_bg_color = "#aa9767"  # RGB values R170 G151 B103
button_fg_color = "#323e48"  # RGB values R50 G62 B72
resolution = "800x480"
mlpershot = 44.36

def oz2ml(oz):
    return 29.574*oz

def authenticate_password():
    # Function to authenticate password from CSV file
    entered_password = password_entry.get()
    with open('assets/users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == entered_password:
                return True, row[1], row[2]  # Password matched, return True and user data
    return False, None, None  # Password not found, return False

def open_main_menu():
    # Function to open the main menu after password authentication
    authenticated, name, balance = authenticate_password()
    if authenticated:
        name_var.set(name)
        balance_var.set(balance)
        root.deiconify()  # Show main menu
        password_window.withdraw()  # Hide password prompt window
    else:
        messagebox.showerror("Error", "Invalid password!")

def enter_digit(digit):
    current_password = password_entry.get()
    current_password += str(digit)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, current_password)

def clear_password():
    password_entry.delete(0, tk.END)

def open_menu(menu_type, name, balance):
    # Close any existing menu windows
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

    # Define variables to keep track of the last pressed shot and amount buttons
    last_shot_button = None
    last_amount_button = None

    def calculate_price(name, shots, amount):
        price = 0
        with open("assets/recipies/"+str(name).replace(" ","")+'.csv') as rfile:
            rreader = csv.reader(rfile)
            for rrow in rreader: 
                if rrow[2]=='true':
                    with open('assets/sources.csv') as sfile:
                        sreader = csv.reader(sfile)
                        for srow in sreader:
                            if srow[0]==rrow[1]:
                                #price #amount #ratio
                                price += float(srow[3])*mlpershot*shots*float(rrow[0])
                if rrow[2]=='false':
                        with open('assets/sources.csv') as sfile:
                            sreader = csv.reader(sfile)
                            for srow in sreader:
                                if srow[0]==rrow[1]:
                                    #price #ratio #mixer amount
                                    price += float(srow[3])*float(rrow[0])*(oz2ml(amount)-(shots*mlpershot))
        return round(price,2)

    def calculate_percentage(name, shots, amount):
        percentage = 0
        with open("assets/recipies/"+str(name).replace(" ","")+'.csv') as rfile:
            rreader = csv.reader(rfile)
            for rrow in rreader: 
                if rrow[2]=='true':
                    with open('assets/sources.csv') as sfile:
                        sreader = csv.reader(sfile)
                        for srow in sreader:
                            if srow[0]==rrow[1]:
                                #percentage #ratio #amount
                                percentage += float(srow[4])*float(rrow[0])*shots*mlpershot
        return round(percentage/oz2ml(amount)*100,1)


    def shot_button_pressed(button):
        nonlocal last_shot_button  
        if last_shot_button:
            last_shot_button.config(bg=button_bg_color, fg=button_fg_color)
        last_shot_button = button
        button.config(bg=button_fg_color, fg=button_bg_color)
        
        # Calculate price and percentage
        if last_amount_button:
            price = calculate_price(drink_entry.get(), int(button["text"]), int(last_amount_button["text"]))
            percentage = calculate_percentage(drink_entry.get(), int(button["text"]), int(last_amount_button["text"]))
            price_entry.config(state="normal")
            percentage_entry.config(state="normal")
            price_entry.delete(0,tk.END)
            price_entry.insert(0,'$'+str(price))
            percentage_entry.delete(0,tk.END)
            percentage_entry.insert(0,str(percentage)+'%')
            price_entry.config(state="readonly",readonlybackground=menu_bg_color)
            percentage_entry.config(state="readonly",readonlybackground=menu_bg_color)

    def amount_button_pressed(button):
        nonlocal last_amount_button
        if last_amount_button:
            last_amount_button.config(bg=button_bg_color, fg=button_fg_color)
        last_amount_button = button
        button.config(bg=button_fg_color, fg=button_bg_color)

        if last_shot_button:
            # Calculate price and percentage
            price = calculate_price(drink_entry.get(), int(last_shot_button["text"]), int(button["text"]))
            percentage = calculate_percentage(drink_entry.get(), int(last_shot_button["text"]), int(button["text"]))
            # Update price and percentage entries
            price_entry.config(state="normal")
            percentage_entry.config(state="normal")
            price_entry.delete(0, tk.END)
            price_entry.insert(0, '$'+str(price))
            percentage_entry.delete(0, tk.END)
            percentage_entry.insert(0, str(percentage)+'%')
            price_entry.config(state="readonly",readonlybackground=menu_bg_color)
            percentage_entry.config(state="readonly",readonlybackground=menu_bg_color)


    menu_window = tk.Toplevel(root)
    menu_window.geometry(resolution)  # Set window size to 680x480 pixels
    menu_window.configure(bg=menu_bg_color)  # Set background color

    # Add name and balance fields at the top of the menu
    name_label = tk.Label(menu_window, text="Name:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(menu_window, state='readonly', textvariable=tk.StringVar(menu_window, value=name), readonlybackground=menu_bg_color, fg=button_bg_color)
    name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    balance_label = tk.Label(menu_window, text="Balance:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    balance_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
    balance_entry = tk.Entry(menu_window, state='readonly', textvariable=tk.StringVar(menu_window, value=balance), readonlybackground=menu_bg_color, fg=button_bg_color)
    balance_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    # Populate the "Drink" field with the name of the menu
    drink_label = tk.Label(menu_window, text="Drink:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    drink_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    drink_entry = tk.Entry(menu_window, bg=menu_bg_color, fg=button_bg_color)
    drink_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    drink_entry.insert(0, menu_type)  # Insert the name of the menu into the "Drink" field
    drink_entry.config(state="readonly",readonlybackground=menu_bg_color)

    # Populate the "Price" field with a default value
    price_label = tk.Label(menu_window, text="Price:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    price_label.grid(row=1, column=2, padx=5, pady=5, sticky="e")
    price_entry = tk.Entry(menu_window, state='readonly', readonlybackground=menu_bg_color, fg=button_bg_color)
    price_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

    # Create buttons for shots
    shots_label = tk.Label(menu_window, text="Shots:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    shots_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    shots_values = ["1", "2", "3", "4", "5"]
    shot_buttons = []
    for i, value in enumerate(shots_values):
        button = tk.Button(menu_window, text=value, width=5, bg=button_bg_color, fg=button_fg_color)
        button.grid(row=2, column=i+1, padx=5, pady=5)
        button.config(command=lambda btn=button: shot_button_pressed(btn))
        shot_buttons.append(button)

    # Create buttons for amount
    amount_label = tk.Label(menu_window, text="Amount (oz):", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    amount_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    amount_values = ["8", "10", "12", "14", "16"]
    amount_buttons = []
    for i, value in enumerate(amount_values):
        button = tk.Button(menu_window, text=value, width=5, bg=button_bg_color, fg=button_fg_color)
        button.grid(row=3, column=i+1, padx=5, pady=5)
        button.config(command=lambda btn=button: amount_button_pressed(btn))
        amount_buttons.append(button)

    # Create read-only text field for alcohol percentage
    percentage_label = tk.Label(menu_window, text="Alcohol Percentage:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
    percentage_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    percentage_entry = tk.Entry(menu_window, state='readonly', readonlybackground=menu_bg_color, fg=button_bg_color)
    percentage_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Create button to dispense drink
    dispense_button = tk.Button(menu_window, text="Dispense Drink", width=20, bg=button_bg_color, fg=button_fg_color)
    dispense_button.grid(row=5, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")

    # Function to dispense drink
    def dispense_drink():
        pass

    # Bind dispense button to dispense function
    dispense_button.config(command=dispense_drink)

    # Create logout button
    logout_button = tk.Button(menu_window, text="Logout", command=lambda: logout(menu_window), bg=button_bg_color, fg=button_fg_color)
    logout_button.grid(row=6, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")

# Create a function to logout
def logout(window):
    window.destroy()  # Close the current submenu window
    password_window.deiconify()  # Bring back the password prompt window


root = tk.Tk()
root.geometry(resolution)  # Set window size to 680x480 pixels
root.configure(bg=menu_bg_color)  # Set background color for the main menu

# Define main menu
name_var = tk.StringVar()
balance_var = tk.StringVar()

name_label_main = tk.Label(root, text="Name:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
name_label_main.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry_main = tk.Entry(root, textvariable=name_var, state='readonly', readonlybackground=menu_bg_color, fg=button_bg_color)
name_entry_main.grid(row=0, column=1, padx=5, pady=5, sticky="w")

balance_label_main = tk.Label(root, text="Balance:", bg=menu_bg_color, fg=button_bg_color, highlightthickness=0)
balance_label_main.grid(row=0, column=2, padx=5, pady=5, sticky="e")
balance_entry_main = tk.Entry(root, textvariable=balance_var, state='readonly', readonlybackground=menu_bg_color, fg=button_bg_color)
balance_entry_main.grid(row=0, column=3, padx=5, pady=5, sticky="w")

# Create password prompt window
password_window = tk.Toplevel(root)
password_window.title("Password")
password_window.geometry(resolution)  # Set window size to 680x480 pixels
password_window.configure(bg=menu_bg_color)  # Set background color for the password menu

password_entry = tk.Entry(password_window, show='*')
password_entry.grid(columnspan=3, padx=5, pady=5)

# Define keypad buttons
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    'Clear', '0', 'Enter'
]

# Populate keypad
for i, button in enumerate(buttons):
    row = i // 3 + 1
    col = (i % 3)
    if button == 'Clear':
        #tk.Button(password_window, text=button, command=clear_password, bg=button_bg_color, fg=button_fg_color, width= 10, height=6).grid(row=row, column=col, padx=5, pady=5)
        tk.Button(password_window, text=button, command=clear_password, bg=button_bg_color, fg=button_fg_color, width= 10, height=6).grid(row=row, column=col, padx=5, pady=5)
    elif button == 'Enter':
        tk.Button(password_window, text=button, command=open_main_menu, bg=button_bg_color, fg=button_fg_color, widt=10, height=6).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(password_window, text=button, command=lambda b=button: enter_digit(b), bg=button_bg_color, fg=button_fg_color, width=10, height=6).grid(row=row, column=col, padx=5, pady=5)

# Hide main menu initially
root.withdraw()

# Define main menu buttons
menu_options = ["SOTB", "Vodka Cran", "Screw Driver", "Jungle Juice",
                "Negroni", "Cosmo", "Margarita", "Cum and Roke"]
for i, option in enumerate(menu_options):
    row = i // 4 * 2 + 1
    col = i % 4
    button = tk.Button(root, text=option, command=lambda o=option: open_menu(o, name_var.get(), balance_var.get()), width=20, height=2, bg=button_bg_color, fg=button_fg_color)
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
