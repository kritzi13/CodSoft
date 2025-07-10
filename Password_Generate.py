import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="❗Enter a number greater than 0")
            return
    except ValueError:
        result_label.config(text="❗Please enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):    
        random_char = random.choice(characters)
        password = password + random_char

    result_label.config(text=f"🔐 Password: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#ffffff")

FONT_TITLE = ("Helvetica", 16, "bold")
FONT_LABEL = ("Helvetica", 10)
FONT_RESULT = ("Courier New", 11, "bold")

title_label = tk.Label(root, text="Secure Password Generator", font=FONT_TITLE, bg="#f5f7fa", fg="#2b2d42")
title_label.pack(pady=15)

length_label = tk.Label(root, text="Password Length:", font=FONT_LABEL, bg="#f5f7fa")
length_label.pack()

length_entry = tk.Entry(root, justify='center', width=10)
length_entry.pack(pady=5)

generate_button = tk.Button(
    root,
    text="Generate",
    command=generate_password,
    bg="#8ecae6",
    fg="white",
    activebackground="#219ebc",
    relief="flat",
    font=FONT_LABEL,
    padx=10,
    pady=5
)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=FONT_RESULT, bg="#f5f7fa", wraplength=350, justify="center")
result_label.pack(pady=10)

root.mainloop()
