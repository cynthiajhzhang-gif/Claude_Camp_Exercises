# 安全计算器

while True:
    print("\n请输入计算（例如：3 + 5），输入 quit 退出")
    user_input = input("> ")
    
    if user_input.lower() == "quit":
        print("再见！")
        break

    try:
        parts = user_input.split()
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "×":
            result = num1 * num2
        elif operator == "÷":
            if num2 == 0:
                print("错误：除数不能为0！")
                continue
            result = num1 / num2
        else:
            print("不支持的运算符！")
            continue

        print(f"结果：{result}")

    except ValueError:
        print("错误：请输入有效数字！")
