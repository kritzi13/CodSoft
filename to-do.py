import customtkinter as ctk
import random

# Theme Setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# App Window
app = ctk.CTk()
app.title("☁️ Task Cloud")
app.geometry("450x600")
app.configure(fg_color="#FAF3E0")

# Fonts and Colors
font_main = ctk.CTkFont("Segoe UI", 14)
font_heading = ctk.CTkFont("Segoe UI", 16, weight="bold")
font_sub = ctk.CTkFont("Segoe UI", 13)
text_color = "#2F2F2F"
task_colors = ["#F8D3DA", "#E9FCD5", "#D1F3F3", "#FDEBD0", "#D7BDE2", "#AED6F1"]

# Store Tasks
tasks = []

# --- Header ---
heading = ctk.CTkLabel(
    app,
    text="Welcome Buddy,\nLet's make today productive!",
    font=font_heading,
    text_color=text_color,
    justify="left"
)
heading.pack(padx=20, pady=(20, 10), anchor="w")

subheading = ctk.CTkLabel(
    app,
    text="Daily Tasks",
    font=font_main,
    text_color=text_color
)
subheading.pack(padx=20, pady=(0, 10), anchor="w")

# --- Scrollable Frame ---
task_list_frame = ctk.CTkScrollableFrame(app, fg_color="#FAF3E0", width=400, height=350)
task_list_frame.pack(padx=10, pady=10, fill="both", expand=True)

# --- Create Task Card ---
def create_task_card(task_text):
    color = random.choice(task_colors)
    card = ctk.CTkFrame(task_list_frame, fg_color=color, corner_radius=10)
    card.pack(fill="x", padx=5, pady=6)

    var = ctk.BooleanVar()
    text_var = ctk.StringVar(value=task_text)

    checkbox = ctk.CTkCheckBox(
        master=card,
        textvariable=text_var,
        variable=var,
        font=font_sub,
        text_color=text_color,
        fg_color="#4B4B4B",
        checkbox_height=20,
        checkbox_width=20
    )
    checkbox.pack(padx=10, pady=10, anchor="w")

    tasks.append((card, checkbox, var, text_var))

# --- Entry & Add Button ---
entry_frame = ctk.CTkFrame(app, fg_color="#FAF3E0")
entry_frame.pack(pady=5)

entry = ctk.CTkEntry(entry_frame, width=260, font=font_sub, placeholder_text="Enter your task")
entry.pack(side="left", padx=5)

def add_task():
    task = entry.get().strip()
    if task:
        create_task_card(task)
        entry.delete(0, "end")

add_btn = ctk.CTkButton(
    entry_frame, text="+", width=40, command=add_task,
    font=font_main, fg_color="#D6A87A", hover_color="#C98E6F"
)
add_btn.pack(side="left")

# --- Actions ---
def delete_task():
    for card, checkbox, var, text_var in tasks[:]:
        if var.get():
            card.destroy()
            tasks.remove((card, checkbox, var, text_var))

def update_task(): # to update the task click on the task then type in the input bar the new task and just click on the update button and your task will change.
    new_text = entry.get().strip()
    if not new_text:
        return
    for card, checkbox, var, text_var in tasks:
        if var.get():
            text_var.set(new_text)
            var.set(False)
            entry.delete(0, "end")
            break

def done_app():
    app.destroy()

# --- Action Buttons ---
btn_frame = ctk.CTkFrame(app, fg_color="#FAF3E0")
btn_frame.pack(pady=(10, 20))

btn_style = {
    "font": font_sub,
    "width": 100,
    "fg_color": "#D6A87A",
    "hover_color": "#C98E6F",
    "text_color": "white"
}

delete_btn = ctk.CTkButton(btn_frame, text="🗑️ Delete", command=delete_task, **btn_style)
update_btn = ctk.CTkButton(btn_frame, text="🔄 Update", command=update_task, **btn_style)
done_btn = ctk.CTkButton(btn_frame, text="✅ Done", command=done_app, **btn_style)

delete_btn.grid(row=0, column=0, padx=10)
update_btn.grid(row=0, column=1, padx=10)
done_btn.grid(row=0, column=2, padx=10)

# --- Run App ---
app.mainloop()

