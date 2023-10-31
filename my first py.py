class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " [Done]"
        else:
            print("Invalid task index")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index")

if __name__ == "__main__":
    todo = TodoList()

    while True:
        print("\nTodo List:")
        todo.list_tasks()

        choice = input("\nChoose an option (add/list/complete/remove/quit): ").strip().lower()

        if choice == "add":
            task = input("Enter a new task: ")
            todo.add_task(task)
        elif choice == "list":
            pass
        elif choice == "complete":
            task_index = int(input("Enter the task number to mark as complete: "))
            todo.complete_task(task_index)
        elif choice == "remove":
            task_index = int(input("Enter the task number to remove: "))
            todo.remove_task(task_index)
        elif choice == "quit":
            break
