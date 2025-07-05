import tkinter as tk
from tkinter import messagebox
import ollama
from ollama import chat
from tkinter import scrolledtext
root = tk.Tk()
root.title('chat')
root.geometry('1000x550')
root.configure(bg="#F5EFFF")

import threading
from ollama import chat

def send_to_ollama():
    user_input = user_entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showerror('error','no prompt found')

    chat_display.config(state='normal')
    chat_display.insert(tk.END, f"You: {user_input}\n")
    chat_display.insert(tk.END, "bot")
    chat_display.config(state='disabled')
    chat_display.see(tk.END)
    user_entry.delete("1.0", tk.END)

    def stream_response():
        try:
            stream = chat(
                model='gemma3:1b',
                messages=[{'role': 'user', 'content': user_input}],
                stream=True
            )

            for chunk in stream:
                content = chunk['message']['content']
                chat_display.after(0, append_response, content)

        except Exception as e:
            chat_display.after(0, append_response, f"\n[Error: {str(e)}]\n")

    threading.Thread(target=stream_response).start()

def append_response(text):
    chat_display.config(state='normal')
    chat_display.insert(tk.END, text)
    chat_display.config(state='disabled')
    chat_display.see(tk.END)


chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12),height = 16,width = 50,bg='#F2F9FF')
chat_display.grid(row=0, column=0, pady=10, columnspan=1)

user_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=('Arial',10,), height = 3, width = 50, bg='#F2F9FF')
user_entry.grid(row=1, column=0)

send_btn = tk.Button(root, text='send', command=send_to_ollama).grid(row=2, column=0)

root.mainloop()