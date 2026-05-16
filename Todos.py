import json

TODO_FILE = "todos.json"

def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f)

def add_todo(todos):
    task = input("请输入待办事项：")
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print("已添加！")

def complete_todo(todos):
    view_todos(todos)
    index = int(input("请输入要完成的编号：")) - 1
    todos[index]["done"] = True
    save_todos(todos)
    print("已完成！")

def view_todos(todos):
    if not todos:
        print("清单为空！")
        return
    for i, todo in enumerate(todos):
        status = "✓" if todo["done"] else "✗"
        print(f"{i+1}. [{status}] {todo['task']}")

todos = load_todos()
while True:
    print("\n1. 添加待办\n2. 完成待办\n3. 查看清单\n4. 退出")
    choice = input("请选择：")
    if choice == "1":
        add_todo(todos)
    elif choice == "2":
        complete_todo(todos)
    elif choice == "3":
        view_todos(todos)
    elif choice == "4":
        break