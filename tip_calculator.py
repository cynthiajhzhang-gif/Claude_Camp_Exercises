print("================================")
print("🍽️  小费计算器")
print("================================")

bill = float(input("请输入餐费金额（元）："))

print("\n请选择小费比例：")
print("1. 10% — 普通服务")
print("2. 15% — 良好服务")
print("3. 20% — 优秀服务")
print("4. 自定义比例")

choice = input("\n请输入选项（1-4）：")

if choice == "1":
    tip_rate = 0.10
elif choice == "2":
    tip_rate = 0.15
elif choice == "3":
    tip_rate = 0.20
else:
    custom = float(input("请输入自定义比例（如输入18代表18%）："))
    tip_rate = custom / 100

people = int(input("\n请输入用餐人数："))

tip = bill * tip_rate
total = bill + tip
per_person = total / people

print(f"""
================================
🧾 消费明细
--------------------------------
💰 餐费金额：{bill:.2f} 元
📊 小费比例：{tip_rate*100:.0f}%
💵 小费金额：{tip:.2f} 元
💳 总计金额：{total:.2f} 元
👥 用餐人数：{people} 人
👤 每人应付：{per_person:.2f} 元
================================
""")