task = []

try:
    with open("tasks.txt", "r") as f:
        for line in f:
            task.append(line.strip())
except FileNotFoundError:
    pass 

while True:
    print(f"<=====Enter Which Option you use=====> \nAdd\nView\nDelete\nExit")
    a = input("Enter Please Your Option 👉  ").lower()
    if a == "add":
        b = input("Enter Your Task 👉 ")
        task.append(b)
        with open("tasks.txt", "w") as f:
            for t in task:
                f.write(t + f"\n")
        print("✅ Task added successfully!")
    elif a == "view":
        if not task:
            print("📭 Your task list is empty.")
        else:
            print("📝 Your To-Do List:")
            for i, t in enumerate(task, 1):
                print(f"{i}. {t}")
    elif a == "delete":
        if not task:
            print("📭 No tasks to delete.")
            continue

        print("🗑️ Your Tasks:")
        for i, t in enumerate(task, 1):
            print(f"{i}. {t}")

        try:
            c = int(input("Enter the task number to delete 👉 "))
            if 1 <= c <= len(task):
                removed = task.pop(c - 1)
                with open("tasks.txt", "w") as f:
                    for t in task:
                        f.write(t + "\n")
                print(f"✅ Task '{removed}' deleted successfully!")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")
    elif a == "exit":
        print("👋 Thanks For Using To-Do-List. Goodbye!")
        break
    else:
        print("❌ Invalid option. Please enter Add, View, Delete, or Exit.")




