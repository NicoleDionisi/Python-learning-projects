import tkinter as tk
import os

tasks = []

if os.path.exists("todo.txt"):
    with open("todo.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]

def refresh_numbers():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        listbox.insert(tk.END, f"{i+1}. {task}")

def complete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        if not task.startswith("✅ "):
            tasks[index] = "✅ " + task
        else:
            tasks[index] = task[3:]
        refresh_numbers()
        with open("todo.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, f"{len(tasks)}. {task}")
        entry.delete(0, tk.END)
        refresh_numbers()
        with open("todo.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        status.config(text="")
    else:
        status.config(text="Please enter a task!")

def edit_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        entry.insert(0, task)
        tasks.pop(index)
        refresh_numbers()
        status.config(text="Edit the task and click Add!")
    else:
        status.config(text="Please select a task first!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        refresh_numbers()
        with open("todo.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")
        status.config(text="")
    else:
        status.config(text="Please select a task first!")


def reset_tasks():
 tasks.clear()
 refresh_numbers()
 with open("todo.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")

window = tk.Tk()
window.title("To Do List")
window.geometry("700x400")
window.resizable(False, False)
window.configure(bg="#ffcece")

label = tk.Label(window, text="To Do List", bg="#ffcece", fg="#c0392b", 
                 font=("Palatino", 25, "bold"), padx=10, pady=5)
label.place(x=10, y=5)

entry = tk.Entry(window, width=30, bg="#fff0f0", fg="#c0392b")
entry.place(x=85, y=80)

def make_button(parent, text, x, y, command):
    frame = tk.Frame(parent, bg="#c0392b")
    frame.place(x=x, y=y)
    btn = tk.Label(frame, text=text, bg="#c0392b", fg="white",
                   padx=10, pady=5, cursor="hand2", font=("Palatino", 11, "bold"))
    btn.bind("<Button-1>", lambda e: command())
    btn.pack()
    return btn

btn_add = make_button(window, "Add", 20, 80, add_task)
btn_delete = make_button(window, "Delete", 20, 230, delete_task)
btn_reset = make_button(window, "Reset", 20, 280, reset_tasks)
btn_complete = make_button(window, "Done", 20, 130, complete_task)
btn_edit = make_button(window, "Edit", 20, 180, edit_task)

listbox = tk.Listbox(window, width=30, height=20, bg="#f9e4a0", fg="black", 
                     relief="flat", selectbackground="#c0392b")
listbox.place(x=390, y=40)
scrollbar = tk.Scrollbar(window)
scrollbar.place(x=660, y=40, height=342)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

status = tk.Label(window, text="", bg="#ffcece", fg="#c0392b", font=("Times new roman", 15))
status.place(x=20, y=330)

for i, task in enumerate(tasks):
    listbox.insert(tk.END, f"{i+1}. {task}")
window.mainloop()