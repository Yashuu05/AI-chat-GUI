import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, Image
from PIL import Image, ImageTk
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, DuplicateKeyError
import os
from dotenv import load_dotenv
# -----------------------------------------------------------------

load_dotenv()
# get mongodb string from the environment
mongo_uri = os.getenv('MONGO_URI')
# create a client
client = MongoClient(mongo_uri)
# select your database name and collection name
db = client["AIChat"]
# collection for user's password and username
users_collection = db['users'] 
# collection for user's name 
name_collection = db['user_name']

    # --- Settings Window and its Functions ---
def open_settings_window():
        # ## FIX: Hide the dashboard instead of destroying it.

        
    settings_win = tk.Toplevel()
    settings_win.title('Settings')
    settings_win.geometry('400x300')
    settings_win.config(bg='#F5EFFF')
    settings_win.grab_set() # ## NEW: Makes this window modal

    def on_settings_close():
    
        settings_win.destroy()
         # Show the dashboard again
        #update_welcome_message() # Update the name in case it was changed
        settings_win.protocol("WM_DELETE_WINDOW", on_settings_close)

# -----------------------------------------------------------------------------------------------------------------------------------
        # --- Sub-windows for Settings ---
        def change_name_window():
            # create new window for changing name
            ########################################################
            name_win = tk.Toplevel(settings_win)
            name_win.title('Change Name')
            name_win.geometry('300x150')
            name_win.config(bg='#F5EFFF')
            name_win.grab_set()

            def save_new_name():
                
                try:
                    # first delete the existing username from database
                    name_collection.delete_many({})
                    # insert the new name of the user in database
                     
                    messagebox.showinfo('Success', f'Name has been changed to {new_name}', parent=name_win)
                    name_win.destroy()
                except ConnectionFailure:
                    messagebox.showerror('Error','Connot connect to Databse!')
                except ConnectionError:
                    messagebox.showerror('Error','Connection Failed!')
                name_win.destroy()

            tk.Label(name_win, text='Enter Your New Name', font=('Georgia', 10, 'bold'), bg='#F5EFFF').pack(pady=10)
            user_input = tk.Entry(name_win, bd=2, width=30)
            user_input.pack(pady=5)
            
            
            tk.Button(name_win, text='Save', command=save_new_name, font=('Georgia', 9, 'bold')).pack(side=tk.LEFT, padx=20, pady=10)
            tk.Button(name_win, text='Cancel', command=name_win.destroy, font=('Georgia', 9, 'bold')).pack(side=tk.RIGHT, padx=20, pady=10)
            #######################################################################################

# ---------------------------------------------------------------------------------------------------------------------------------
        # second button to change the credentials
        def change_password_window():
            # ## FIX: Complete rewrite of the password change logic for clarity and correctness.
            ###################################################
            auth_win = tk.Toplevel(settings_win)
            auth_win.title('Authenticate')
            auth_win.geometry('400x200')
            auth_win.config(bg='#F5EFFF')
            auth_win.grab_set()

            def verify_and_proceed():
                entered_pass = pass_entry.get()
                if entered_pass == valid_pass:
                    auth_win.destroy()
                    open_credential_editor()
                else:
                    messagebox.showerror("Error", "Incorrect password.", parent=auth_win)

            def open_credential_editor():
                global valid_username, valid_pass
                cred_win = tk.Toplevel(settings_win)
                cred_win.title("Change Credentials")
                cred_win.geometry('400x200')
                cred_win.config(bg='#F5EFFF')
                cred_win.grab_set()

                def save_new_credentials():
                    new_user = new_username_entry.get().strip()
                    new_pwd = new_pass_entry.get().strip()
                    if not new_user or not new_pwd:
                        messagebox.showwarning("Warning", "Fields cannot be empty.", parent=cred_win)
                        return

                    credentials["username"] = new_user
                    credentials["password"] = new_pwd
                    with open('credentials.json', 'w') as f:
                        json.dump(credentials, f, indent=4)
                    
                    # Update globals
                    valid_username = new_user
                    valid_pass = new_pwd
                    
                    messagebox.showinfo('Success', 'Credentials updated successfully.', parent=cred_win)
                    cred_win.destroy()
                
                tk.Label(cred_win, text='New Username', font=('Georgia', 9), bg='#F5EFFF').grid(row=0, column=0, padx=10, pady=10, sticky='w')
                new_username_entry = tk.Entry(cred_win)
                new_username_entry.grid(row=0, column=1, padx=10, pady=10)
                new_username_entry.insert(0, valid_username)

                tk.Label(cred_win, text='New Password', font=('Georgia', 9), bg='#F5EFFF').grid(row=1, column=0, padx=10, pady=10, sticky='w')
                new_pass_entry = tk.Entry(cred_win, show='*')
                new_pass_entry.grid(row=1, column=1, padx=10, pady=10)
                new_pass_entry.insert(0, valid_pass)

                tk.Button(cred_win, text='Confirm', command=save_new_credentials, font=('Georgia', 10, 'bold')).grid(row=2, column=1, padx=10, pady=20, sticky='e')
                tk.Button(cred_win, text='Cancel', command=cred_win.destroy, font=('Georgia', 10, 'bold')).grid(row=2, column=0, padx=10, pady=20, sticky='w')
                ##################################################################################################


            tk.Label(auth_win, text='Enter current password to continue', font=('Georgia', 12, 'bold'), bg='#F5EFFF').pack(pady=15)
            pass_entry = tk.Entry(auth_win, bd=2, show='*')
            pass_entry.pack(pady=5, padx=20, fill='x')
            
            tk.Button(auth_win, text='Verify', command=verify_and_proceed, font=('Georgia', 10, 'bold')).pack(side='left', padx=30, pady=10)
            tk.Button(auth_win, text='Cancel', command=auth_win.destroy, font=('Georgia', 10, 'bold')).pack(side='right', padx=30, pady=10)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

        # --- Settings Window Widgets ---
        tk.Label(settings_win, text='User Settings', font=('Courier', 14, 'bold'), bg='#F5EFFF').grid(row=0, column=0,  padx=10, pady=10, sticky='w')
        
        tk.Button(settings_win, text='Change Name', command=change_name_window, font=('Georgia', 10)).grid(row=1, column=0, padx=20, pady=10, sticky='ew')
        tk.Button(settings_win, text='Change Credentials', command=change_password_window, font=('Georgia', 10)).grid(row=2, column=0, padx=20, pady=10, sticky='ew')
        
        tk.Button(settings_win, text='Back', font=('Courier', 10, 'bold'), command=on_settings_close).grid(row=2, column=1, padx=10, pady=20, sticky='se')
        settings_win.grid_columnconfigure(1, weight=1) # Makes the back button stick to the right

        tk.Label(settings_win, text="developed by", font=('courier',14,'bold'), bg='#F5EFFF').grid(row=0,column=1,padx=10,pady=10)

        logo_img = Image.open("logo_1.png").resize((84,84), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(logo_img)
        image_label = tk.Label(settings_win, image=logo, bg='#F5EFFF')
        image_label.image = logo
        image_label.grid(row=1, column=1, padx=10, pady=10)
