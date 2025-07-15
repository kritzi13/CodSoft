import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        save_contacts()
        show_contacts()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required.")

def show_contacts():
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        contact_list.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for i, c in enumerate(contacts):
        if query in c["name"].lower() or query in c["phone"]:
            contact_list.insert(tk.END, f"{i+1}. {c['name']} - {c['phone']}")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contacts.pop(selected[0])
        save_contacts()
        show_contacts()

def update_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]

        new_name = simpledialog.askstring("Update Name", "New name:", initialvalue=contact["name"])
        new_phone = simpledialog.askstring("Update Phone", "New phone:", initialvalue=contact["phone"])
        new_email = simpledialog.askstring("Update Email", "New email:", initialvalue=contact["email"])
        new_address = simpledialog.askstring("Update Address", "New address:", initialvalue=contact["address"])

        if new_name and new_phone:
            contacts[index] = {
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            }
            save_contacts()
            show_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required.")

def clear_entries():
    for e in [name_entry, phone_entry, email_entry, address_entry, search_entry]:
        e.delete(0, tk.END)


contacts = load_contacts()
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x550")


tk.Label(root, text="📒 Contact Log", font=("Arial", 18, "bold")).pack(pady=10)


form = tk.Frame(root)
form.pack(pady=5)


tk.Label(form, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(form, width=20)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(form, text="Phone").grid(row=0, column=2, padx=5, pady=5)
phone_entry = tk.Entry(form, width=20)
phone_entry.grid(row=0, column=3, padx=5)


tk.Label(form, text="Email").grid(row=1, column=0, padx=5, pady=5)
email_entry = tk.Entry(form, width=20)
email_entry.grid(row=1, column=1, padx=5)

tk.Label(form, text="Address").grid(row=1, column=2, padx=5, pady=5)
address_entry = tk.Entry(form, width=20)
address_entry.grid(row=1, column=3, padx=5)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", width=15, command=add_contact).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Update Contact", width=15, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete Contact", width=15, command=delete_contact).grid(row=1, column=0, padx=5)
tk.Button(btn_frame, text="Show All", width=15, command=show_contacts).grid(row=1, column=1, padx=5)


tk.Label(root, text="Search by Name or Phone").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)


contact_list = tk.Listbox(root, width=60, height=10)
contact_list.pack(pady=15)

show_contacts()
root.mainloop()
