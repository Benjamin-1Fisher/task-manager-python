import tkinter as tk
from tkinter import messagebox
from main import save_tasks, load_tasks

tasks = load_tasks()


def add_task():
    task_name = entry.get()
    if task_name == "":
        messagebox.showinfo("Error", "Please enter name of the task")
        return

    if task_name != "":
        tasks.append({"name": task_name, "done": False, "pinned": False})
        save_tasks(tasks)
        listbox.insert(tk.END, task_name)
        entry.delete(0, tk.END)
        refresh_listbox()


def remove_task():
    selected_tasks = listbox.curselection()
    
    if not selected_tasks:
        messagebox.showinfo("Error", "Please select a task")
        return

    for index in reversed(selected_tasks):
        tasks.pop(index)

    save_tasks(tasks)
    refresh_listbox()
        

def remove_all_tasks():
    if len(tasks) != 0:
        answer = messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?")
        
        if answer:
            tasks.clear()
            save_tasks(tasks)
            refresh_listbox()    
    else:
        answer = messagebox.showinfo("","No tasks to remove")
    

def refresh_listbox():
    listbox.delete(0, tk.END)

    tasks.sort(key=lambda task: task["pinned"], reverse=True)

    for task in tasks:
        status = "Done" if task["done"] else "Not done"
        pin_status = "📌 " if task["pinned"] else ""
        listbox.insert(tk.END, f'{pin_status}{task["name"]} - {status}')
        
        
def mark_task_done():
    selected_tasks = listbox.curselection()
    
    if not selected_tasks:
        messagebox.showinfo("Error", "Please select a task")
        return

    for index in selected_tasks:
        tasks[index]["done"] = True
        
    save_tasks(tasks)
    refresh_listbox()


def mark_task_not_done():
    selected_tasks = listbox.curselection()
    
    if not selected_tasks:
        messagebox.showinfo("Error", "Please select a task")
        return

    for index in selected_tasks:
        tasks[index]["done"] = False
        
    save_tasks(tasks)
    refresh_listbox()


def pin_task():
    selected_tasks = listbox.curselection()
    
    if not selected_tasks:
        messagebox.showinfo("Error", "Please select a task")
        return

    for index in selected_tasks:
        tasks[index]["pinned"] = False
        
    save_tasks(tasks)
    refresh_listbox()



def unpin_task():
    selected_task = listbox.curselection()
    if not selected_task:
        messagebox.showinfo("Error", "Please select a task")
        return

    elif selected_task:
        index = selected_task[0]
        tasks[index]["pinned"] = False
        tasks.sort(key=lambda task: task["pinned"], reverse=True)
        save_tasks(tasks)
        refresh_listbox()


def edit_task():
    selected_tasks = listbox.curselection()

    if len(selected_tasks) == 0:
        messagebox.showinfo("Error", "Please select one task to edit.")
        return

    if len(selected_tasks) > 1:
        messagebox.showinfo("Error", "Please select only one task to edit.")
        return

    index = selected_tasks[0]

    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Task")
    edit_window.geometry("300x150")

    edit_label = tk.Label(edit_window, text="Edit task name:")
    edit_label.pack(pady=10)

    edit_entry = tk.Entry(edit_window, width=30)
    edit_entry.pack(pady=10)
    edit_entry.insert(0, tasks[index]["name"])

    def save_edited_task():
        new_name = edit_entry.get()

        if new_name == "":
            messagebox.showinfo("Error", "Task name cannot be empty.")
            return

        tasks[index]["name"] = new_name
        save_tasks(tasks)
        refresh_listbox()
        edit_window.destroy()

    save_button = tk.Button(edit_window, text="Save", command=save_edited_task)
    save_button.pack(pady=10)
    
window = tk.Tk()    
window.configure(bg="#f4f4f4")
window.title("Task Manager")
window.geometry("500x650")
window.configure(padx=20, pady=20)

title_label = tk.Label(window, text="Task Manager", font=("Arial", 20, "bold"), bg="#f4f4f4")
title_label.pack(pady=15)

tasks_label = tk.Label(window, text="Your Tasks", font=("Arial", 12, "bold"))
tasks_label.pack(pady=10)

entry = tk.Entry(window, width=35, font=("Arial", 12))
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task, width=25, bg="#d9ead3")
add_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Selected Task", command=remove_task, width=25, bg="#d9ead3")
remove_button.pack(pady=5)

remove_all_tasks_button = tk.Button(window, text="Remove all tasks", command=remove_all_tasks, width=25, bg="#d9ead3")
remove_all_tasks_button.pack(pady=5)

mark__done_button = tk.Button(window, text="Mark selected task as done", command=mark_task_done, width=25, bg="#d9ead3")
mark__done_button.pack(pady=5)

mark_not_done_button = tk.Button(window, text="Mark selected task as not done", command=mark_task_not_done, width=25, bg="#d9ead3")
mark_not_done_button.pack(pady=5)

pin_button = tk.Button(window, text="Pin Selected Task", command=pin_task, width=25, bg="#d9ead3")
pin_button.pack(pady=5)

unpin_button = tk.Button(window, text="Unpin Selected Task", command=unpin_task, width=25, bg="#d9ead3")
unpin_button.pack(pady=5)

edit_task_button = tk.Button(window, text="Edit Selected Task", command=edit_task, width=25, bg="#d9ead3")
edit_task_button.pack(pady=5)

listbox = tk.Listbox(window, width=50, height=15, selectmode=tk.MULTIPLE, font=("Arial", 11))
listbox.pack(pady=15)

refresh_listbox()
      
window.mainloop()