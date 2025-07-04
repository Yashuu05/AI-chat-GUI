# import libraries and modules
import tkinter as tk
from tkinter import messagebox
from pymongo.errors import ConnectionFailure
from ollama import chat
from tkinter import scrolledtext
from tkinter import PhotoImage, Image
from PIL import Image, ImageTk
# ---------------------------------------------------
def dashboard_window():
    # create window 
    window = tk.Toplevel()
    # size of window
    window.geometry('1000x550')
    # background color
    window.configure(bg="#F5EFFF")
    # title of window
    window.title('Chat Interface')
    #------------------------------------------------------
    # button to clear
    def clear():
        user_field.delete('1.0', tk.END)

    # logout button
    def logout():
        window.destroy()

    # heading
    tk.Label(window, text="How I can help you today?", bg='#F5EFFF',font=('comic sans ms',14,'italic')).grid(row=0, column=0,padx=10, pady=10, columnspan=3)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    # AI respone entry
    chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12),height = 16,width = 50,bg='#F2F9FF')
    chat_display.grid(row=1, column=1, pady=10, columnspan=1)

    # user input field
    user_field = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=('Arial',10,), height = 3, width = 50, bg='#F2F9FF')
    user_field.grid(row=2, column=1)

    # send button
    try:
        send_img = Image.open('send_icon.png')
        send_img = send_img.resize((43,43), Image.Resampling.LANCZOS)
        send_img = ImageTk.PhotoImage(send_img)
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Failed to load image: {e}")
        send_img = None
    send_btn = tk.Button(window, image=send_img)
    send_btn.image = send_img
    send_btn.grid(row=2, column=2, padx=10, pady=10)

    # clear button
    clear_btn = tk.Button(window, text='clear', width=15, command=clear, font=('Arial',10,'bold'), bg='#FCFFC1')
    clear_btn.grid(row=2, column=0)

    # logout button
    logout_btn = tk.Button(window, text='Logout', command=logout, bg='#F7374F', fg='white', font=('Arial',10,'bold'), width=20)
    logout_btn.grid(row=0, column=2)