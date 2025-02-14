todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added!")

def remove_task(index):
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid index.")

def show_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        index = int(input("Enter task number to remove: ")) - 1
        remove_task(index)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Exiting the app.")
        break
    else:
        print("Invalid choice.")
