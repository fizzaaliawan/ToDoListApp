import os

def load_tasks(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    tasks.append({
                        "name": parts[0],
                        "status": parts[1],
                        "deadline": parts[2]
                    })
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['status']}|{task['deadline']}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return
    print("\nYour Tasks:")
    print(f"{'No.':<4} {'Task':<25} {'Status':<10} {'Deadline':<12}")
    print("-" * 55)
    for idx, task in enumerate(tasks, 1):
        print(f"{idx:<4} {task['name']:<25} {task['status']:<10} {task['deadline']:<12}")
    print()


def add_task(tasks):
    name = input("Enter task name: ")
    deadline = input("Enter deadline (optional, e.g., 2025-09-01) or leave blank: ")
    if not deadline:
        deadline = "N/A"
    tasks.append({"name": name, "status": "Pending", "deadline": deadline})
    print(f"Task '{name}' added successfully!\n")


def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed['name']}' deleted successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")


def mark_done(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["status"] = "Done"
                print(f"Task '{tasks[num - 1]['name']}' marked as done!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")


def main():
    tasks = load_tasks()
    
    while True:
        print("===== TO-DO LIST APP =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.\n")

if __name__ == "__main__":
    main()
