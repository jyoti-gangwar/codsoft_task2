import tkinter as tk
from tkinter import messagebox
import random
import string
# Generate Password
def generate_password():
    length = length_entry.get().strip()
    if length == "":
        messagebox.showwarning("Warning", "Please enter password length.")
        return
    if not length.isdigit():
        messagebox.showerror("Error", "Length must be a number.")
        return
    length = int(length)
    if length < 4:
        messagebox.showwarning("Warning", "Minimum length should be 4.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")
# Clear Fields
def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")
# Main Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("450x300")
window.config(bg="#F4F4F4")
window.resizable(False, False)
title = tk.Label(
    window,
    text="PASSWORD GENERATOR",
    font=("Arial", 18, "bold"),
    fg="navy",
    bg="#F4F4F4"
)
title.pack(pady=15)
label = tk.Label(
    window,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="#F4F4F4"
)
label.pack()
length_entry = tk.Entry(window, font=("Arial", 12), width=20)
length_entry.pack(pady=8)
generate_btn = tk.Button(
    window,
    text="Generate Password",
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    width=18,
    command=generate_password
)
generate_btn.pack(pady=10)
password_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=32,
    justify="center",
    state="readonly"
)
password_entry.pack(pady=10)
clear_btn = tk.Button(
    window,
    text="Clear",
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12,
    command=clear_fields
)
clear_btn.pack(pady=10)
window.mainloop()