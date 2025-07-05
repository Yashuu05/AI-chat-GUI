# import libraries and modules
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure
import os
import board
# -------------------------------------------------------------------------
# database connection 
# load data from .env file
load_dotenv()
# Read MongoDB URI from environment
mongo_uri = os.getenv("MONGO_URI")
# create client to connect to your MongoDB Atlas string
client = MongoClient(mongo_uri)
# select your database name and collection name
db = client["AIChat"]
# collection for user's password and username
users_collection = db['users'] 
# --------------------------------------------------------------------------

# create login window
root = tk.Tk()
root.title('Login Form')
root.geometry('400x250')
root.configure(bg="#F5EFFF")
# --------------------------------------------------------------------------

# function to toggle hide / show button
def toggle_password_visibility():
    # ## FIX: Renamed function
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        show_pass_button.config(text='Hide Password')
    else:
        password_entry.config(show='*')
        show_pass_button.config(text='Show Password')

# function for login logic
def login():
    # get user input from input fields
    username = username_entry.get()
    password = password_entry.get()
    try:
        user = users_collection.find_one({"username": username, "password": password})
        if user:
            messagebox.showinfo('info','login successful')
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            # withdraw the login window
            root.withdraw()
            # open password manager window
            board.window_of_dashboard(root)
        elif username == '' and password == '':
            messagebox.showerror('Error','Enter Credentials to proceed')
        else:
            messagebox.showerror('Error','invalid credentials')
    except ConnectionFailure:
        messagebox("Eorror"," cannot connect to database")
    except ConnectionError:
        messagebox.showerror("Error","Connection Error!")
# ------------------------------------------------------------------------------------------------------------

# main page widgets

# heading
heading = tk.Label(root, text='AI Chat Interface', font=('Times New Roman', 16, 'italic'), bg='#F5EFFF')
heading.pack(pady=20)

# login frame
login_frame = tk.Frame(root, bg="#F5EFFF")
login_frame.pack(padx=10, pady=10)

# username entry and label    
username_label = tk.Label(login_frame, text='Username', bg='#F5EFFF', font=('Arial', 12))
username_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
username_entry = tk.Entry(login_frame, bd=2, font=('courier', 10), width=25)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# password entry and label
password_label = tk.Label(login_frame, text='Password', bg='#F5EFFF', font=('Arial', 12))
password_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
password_entry = tk.Entry(login_frame, bd=2, show='*', font=('courier', 10), width=25)
password_entry.grid(row=1, column=1, padx=5, pady=5)

# 'show password' button
show_pass_button = tk.Button(login_frame, text='Show Password', command=toggle_password_visibility, font=('Georgia', 9))
# ## FIX: Corrected typo in function name
show_pass_button.grid(row=2, column=1, pady=5, sticky='w')

# login button
login_button = tk.Button(root, text='Go', command=login, bg='#CDC1FF', fg='black', font=('Georgia', 12, 'bold'), width=10)
login_button.pack(pady=10)
    
# Allow hitting 'Enter' to log in
root.bind('<Return>', lambda event=None: login_button.invoke())

# run the main window
root.mainloop()