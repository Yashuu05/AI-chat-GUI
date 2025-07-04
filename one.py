import tkinter as tk
import two
root = tk.Tk()
root.title('one')
root.geometry('200x150')
second_win = two.second
tk.Button(root, text='click',command=second_win).pack(pady=10)
tk.mainloop()