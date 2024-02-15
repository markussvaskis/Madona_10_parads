import tkinter as tk
from tkinter import filedialog
import os
def browse_file():
 file_path = filedialog.askopenfilename()
 file_field.delete(0, tk.END)
 file_field.insert(tk.END, file_path)
 
def read_file():
 file_path = file_field.get()
 if file_path:
  if os.path.exists(file_path):
   with open(file_path, 'r') as f:
    file_contents = f.read()
    print(file_contents)
 else:
    print("failu nevareja atrast.") 
 
    print("ievadiet faila lokaciju.")
 
root = tk.Tk()
root.title("fails")

file_field = tk.Entry(root, width=50)
file_field.pack()

browse_button = tk.Button(root, text="meklet failu", command=browse_file)
browse_button.pack()

read_button = tk.Button(root, text="lasit failu", command=read_file)
read_button.pack()

root.mainloop()