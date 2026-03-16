import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def get_tasks_file():
    if getattr(sys, 'frozen', False):
        # אם זה exe
        base_path = os.path.dirname(sys.executable)
    else:
        # אם מריצים עם python
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "tasks.json")


def save_tasks(tasks):
    tasks_file = get_tasks_file()
    with open(tasks_file, "w") as file:
        json.dump(tasks, file)


def load_tasks():
    tasks_file = get_tasks_file()

    try:
        with open(tasks_file, "r") as file:
            tasks = json.load(file)

            for task in tasks:
                if "pinned" not in task:
                    task["pinned"] = False

            return tasks
    except FileNotFoundError:
        return []



def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add task.")
    print("2. remove task.")
    print("3. Show tasks.")
    print("4. Mark task as done.")
    print("5. Mark task not done")
    print("6. Exit.")


def add_task(tasks):
    task_name = input("Enter task name: ")
    tasks.append({"name": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")
    

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("Enter task number to remove: "))
    except ValueError:
        print("Invalid input.")
        return

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['name']}' removed.")
    else:
        print("Invalid task number.")
        

def remove_all_tasks(tasks):
    print()
    print("Please confirm to Remove all tasks?" , end = "")
    print("\n1. Yes")
    print("2. No")
    answer = input("Enter choise number: ")
    
    if answer == "1":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks removed.")
    elif answer == "2":
        print("Cancelled.")
    else:
        print("invalid choise.")
    
    
def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            if tasks[i]["done"] == True:
                status = "Done"
            else:
                status = "Not done"

            print(f"{i + 1}. {tasks[i]['name']} - {status}")
            print()
            

def mark_task_done(tasks):
    if len(tasks) == 0:
        print("No tasks to mark.")
        return

    show_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as done: "))
    except:
        print("invalid input.")
        return
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task number.")
        
        
def mark_task_not_done(tasks):
    if len(tasks) == 0:
        print("No tasks to mark.")
        return
    
    show_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as not done: "))
    except:
        print("invalid input.")
        return
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = False
        save_tasks(tasks)
        print("Task marked as not done.")
    else:
        print("Invalid task number.")
    


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option number: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:    
                print("\n1. Remove one task.")
                print("2. Remove all tasks.")
                print("3. Back.")
                
                remove_choic = input("Choose an aption: ")
                
                if remove_choic == "1":
                    remove_task(tasks)
                elif remove_choic == "2":
                    remove_all_tasks(tasks)
                elif remove_choic == "3":
                    continue
                else:
                    print("invalid choice.")
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            mark_task_not_done(tasks)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()