import time
import board
import busio
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint
import csv
import mainMenu

# Path to the CSV file
CSV_FILE = 'user_data.csv'

# Define CSV fieldnames
FIELDNAMES = ['user_id', 'name', 'balance', 'total_alcohol_purchased']

# Initialize fingerprint sensor
uart = busio.UART(board.TX, board.RX, baudrate=57600)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

# Load existing user data from CSV file
try:
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        user_data = {int(row['user_id']): {key: float(row[key]) if key != 'name' else row[key] for key in row} for row in reader}
except FileNotFoundError:
    # If file doesn't exist, initialize an empty user_data dictionary
    user_data = {}

# Function to save user data to CSV file
def save_user_data():
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for user_id, data in user_data.items():
            writer.writerow({'user_id': user_id, **data})

# Function to enroll a new user
def enroll_user(user_id, name):
    user_data[user_id] = {
        'name': name,
        'balance': 0.0,  # Initial balance
        'total_alcohol_purchased': 0.0  # Initial total alcohol purchased
    }
    save_user_data()

# Function to get user data
def get_user_data(user_id):
    return user_data.get(user_id)

# Function to update user data
def update_user_data(user_id, key, value):
    if user_id in user_data:
        user_data[user_id][key] = value
        save_user_data()
        return True
    return False

# Function to authenticate user via fingerprint
def authenticate_user():
    print("Waiting for fingerprint...")
    while True:
        if finger.get_image() == adafruit_fingerprint.OK:
            print("Fingerprint detected!")
            if finger.image_2_tz(1) == adafruit_fingerprint.OK:
                if finger.finger_fast_search() == adafruit_fingerprint.OK:
                    print("Fingerprint matched!")
                    return finger.finger_id
                else:
                    print("Fingerprint not recognized.")
            else:
                print("Fingerprint could not be processed.")
        time.sleep(0.1)

# Function to open the application associated with the authenticated user
def open_application(user_id):
    user = user_data.get(user_id)
    if user:
        print(f"Opening application for user: {user['name']}")
        mainMenu(user['name'],user['balance'])
    else:
        print("User not found.")

if __name__ == "__main__":
    while True:
        user_id = authenticate_user()
        if user_id:
            open_application(user_id)
            break  # Exit the loop after successful authentication and application opening
        else:
            print("Authentication failed.")
