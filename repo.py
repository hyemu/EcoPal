import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import datetime

def dispose_bottle():
    if not is_user_logged_in():
        show_login_message()
        return
    
    dispose_window = tk.Toplevel()
    dispose_window.title("Dispose Bottle")
    dispose_window.geometry("300x200")
    
    kilos_label = tk.Label(dispose_window, text="Kilos:")
    kilos_label.pack()
    kilos_entry = tk.Entry(dispose_window)
    kilos_entry.pack(pady=5)
    
    packs_label = tk.Label(dispose_window, text="Packs:")
    packs_label.pack()
    packs_entry = tk.Entry(dispose_window)
    packs_entry.pack(pady=5)
    
    def save_disposal():
        kilos = kilos_entry.get()
        packs = packs_entry.get()
        
        # Save disposal data to a file
        with open("disposal_data.txt", "a") as file:
            file.write(f"{kilos},{packs}\n")
        
        dispose_window.destroy()
        update_bottle_count()
    
    save_button = tk.Button(dispose_window, text="Save", command=save_disposal)
    save_button.pack(pady=10)

def redeem_reward():
    if not is_user_logged_in():
        show_login_message()
        return
    
    # Code to handle reward redemption
    pass

def update_bottle_count():
    # Code to update bottle count label
    # Here, you can implement the logic to fetch the updated bottle count and display it
    bottle_count = 10  # Example value, replace with actual value
    bottle_count_label.config(text="Bottles Disposed: " + str(bottle_count))

def is_user_logged_in():
    # Code to check if user is logged in
    # Here, you can implement the logic to determine if the user is logged in
    # For example, you can check if a user session exists or if user credentials are stored
    
    return logged_in_user.get() != ""

def show_login_message():
    login_message = messagebox.showinfo("Login Required", "Please login to continue.")

def login_window():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        # Check login credentials
        if check_login_credentials(username, password):
            logged_in_user.set(username)
            messagebox.showinfo("Login", f"Logged in as {username}")
            login_window.destroy()
            update_username_label()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    login_window = tk.Toplevel()
    login_window.title("Login")

    # Create and pack username label and entry
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    # Create and pack password label and entry
    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    # Create and pack login button
    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=10)

def register_window():
    def register():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        
        # Save registration data to a file or process the registration
        save_registration_data(username, password, email)
        
        messagebox.showinfo("Registration", f"Registered user: {username}")
        register_window.destroy()

    register_window = tk.Toplevel()
    register_window.title("Register")

    # Create and pack username label and entry
    username_label = tk.Label(register_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    # Create and pack password label and entry
    password_label = tk.Label(register_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack(pady=5)

    # Create and pack email label and entry
    email_label = tk.Label(register_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack(pady=5)

    # Create and pack register button
    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.pack(pady=10)

def check_login_credentials(username, password):
    # Code to check login credentials against saved data
    # Here, you can implement the logic to compare the entered username and password
    # with the saved data from the registration process
    # Return True if the credentials match, False otherwise
    # Example implementation:
    with open("registration_data.txt", "r") as file:
        for line in file:
            saved_username, saved_password, _ = line.strip().split(",")
            if username == saved_username and password == saved_password:
                return True
    return False

def save_registration_data(username, password, email):
    # Save registration data to a file
    with open("registration_data.txt", "a") as file:
        file.write(f"{username},{password},{email}\n")

def update_username_label():
    username = logged_in_user.get()
    username_label.config(text="Logged in as: " + username if username else "Not logged in")

# Create the main window
window = tk.Tk()
window.title("Water Bottle Disposal Reward System")
window.geometry("400x450")

# Set background color
window.configure(bg="#FFFFFF")

# Variable to store the logged-in user
logged_in_user = tk.StringVar()
logged_in_user.set("")  # Initialize with an empty string

# Create labels
bottle_count_label = tk.Label(window, text="Bottles Disposed: 0", font=("Arial", 12))
bottle_count_label.pack(pady=10)

# Create current date and time label
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
datetime_label = tk.Label(window, text="Current Date and Time: " + current_datetime, font=("Arial", 12))
datetime_label.pack(pady=10)

# Create buttons
dispose_button = tk.Button(window, text="Dispose Bottle", command=dispose_bottle, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 12))
dispose_button.pack(pady=10)

redeem_button = tk.Button(window, text="Redeem Reward", command=redeem_reward, bg="#FF5722", fg="#FFFFFF", font=("Arial", 12))
redeem_button.pack(pady=10)

# Create login and register buttons
login_button = tk.Button(window, text="Login", command=login_window, bg="#2196F3", fg="#FFFFFF", font=("Arial", 12))
login_button.pack(pady=5)

register_button = tk.Button(window, text="Register", command=register_window, bg="#FF9800", fg="#FFFFFF", font=("Arial", 12))
register_button.pack(pady=5)

# Create username label
username_label = tk.Label(window, text="Not logged in", font=("Arial", 12))
username_label.pack(pady=10)

# Run the main loop
window.mainloop()
