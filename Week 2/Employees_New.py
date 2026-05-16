# 员工名册管理器

employees = {}

def add_employee():
    name = input("请输入姓名: ")
    email = input("请输入邮箱: ")
    phone = input("请输入电话: ")
    start_date = input("请输入入职日期: ")
    employees[name] = {"name": name, "email": email, "phone": phone, "start_date": start_date}
    print("员工添加成功！")

def search_employee():
    name = input("请输入要查询的姓名: ")
    if name in employees:
        for key, value in employees[name].items():
            print(f"{key}: {value}")
    else:
        print("员工不存在")

def delete_employee():
    name = input("请输入要删除的姓名: ")
    if name in employees:
        del employees[name]
        print("删除成功")
    else:
        print("员工不存在")

while True:
    try:
        print("""
请选择操作：
1. 添加员工
2. 查询员工
3. 删除员工
4. 退出
        """)
        choice = int(input("请输入选择: "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            search_employee()
        elif choice == 3:
            delete_employee()
        elif choice == 4:
            print("再见！")
            break
        else:
            print("无效选项，请重新输入")
    except ValueError:
        print("请输入有效数字！")
