import tkinter as tk
from tkinter import messagebox, font

def add_task():
    task = entry.get()
    if task.strip():
        tasks_listbox.insert(tk.END, f"✅ {task}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Please enter a task.")

def delete_task():
    selected = tasks_listbox.curselection()
    if selected:
        tasks_listbox.delete(selected)
        messagebox.showinfo("❌ Deleted", "Task deleted successfully!")
    else:
        messagebox.showwarning("⚠ Warning", "No task selected.")

def view_tasks():
    count = tasks_listbox.size()
    if count == 0:
        messagebox.showinfo("📋 Tasks", "ᴛʜᴇʀᴇ ɪꜱ ɴᴏ ᴛᴀꜱᴋꜱ")
    else:
        tasks = "\n".join(tasks_listbox.get(0, tk.END))
        messagebox.showinfo("📋 Your Tasks", tasks)

root = tk.Tk()
root.title("█▓▒▒░░░ZOZ TO DO LIST░░░▒▒▓█")
root.geometry("400x700")  
root.configure(bg="black")
root.resizable(True, True)

app_font = font.Font(family="Arial", size=12, weight="bold")

title_label = tk.Label(root, text="ZOZ TO DO LIST 📋", bg="black", fg="white", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

entry = tk.Entry(root, font=app_font, bg="#1e1e1e", fg="white", insertbackground="white", relief="flat")
entry.pack(pady=10, ipady=5, ipadx=5, fill="x", padx=20)

button_style = {
    "font": app_font,
    "bg": "#333333",
    "fg": "white",
    "activebackground": "green",
    "activeforeground": "white",
    "relief": "flat",
    "cursor": "hand2",
    "bd": 0,
    "highlightthickness": 0,
    "padx": 10,
    "pady": 8
}

btn_add = tk.Button(root, text="➕ ᴀᴅᴅ ᴛᴀꜱᴋ", command=add_task, **button_style)
btn_add.pack(pady=5, fill="x", padx=20)

btn_view = tk.Button(root, text="📄 ᴠɪᴇᴡ ᴛᴀꜱᴋꜱ", command=view_tasks, **button_style)
btn_view.pack(pady=5, fill="x", padx=20)

btn_delete = tk.Button(root, text="❌ ᴅᴇʟᴇᴛᴇ ᴛᴀꜱᴋ", command=delete_task, **button_style)
btn_delete.pack(pady=5, fill="x", padx=20)

tasks_listbox = tk.Listbox(root, font=app_font, bg="#1e1e1e", fg="white", selectbackground="green", activestyle="none", relief="flat")
tasks_listbox.pack(pady=10, fill="both", expand=True, padx=20)


root.mainloop()
