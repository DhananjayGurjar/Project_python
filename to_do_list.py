# A command-line app where you can add, view, delete,
# and mark tasks as done — basically a mini task manager that runs in the terminal.

print("Welcome to the TO DO LIST APP\n\t")


tasks = []


def add_task():
    list.append(input("Enter Your task:"))
    # pasṇs


def view_task():
    for i in range(len(list)):
        print(list[i])

 
def delete_task():
    remove_task = input("Enter Your task to remove:")
    print(list.remove(remove_task))


for i in range(100):
    print("1. add task")
    print("2. remove task")
    print("3. view tasks")
    print("4.exit\n")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        add_task()
        print("Task added \n")

    elif choice == 2:
        delete_task()
        print("Task deleted \n")
    elif choice == 3:
        view_task()
        print("Thank You")
        break
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid choice\n")
