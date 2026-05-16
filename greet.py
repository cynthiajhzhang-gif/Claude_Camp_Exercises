name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
age = int(age)

if age < 18:
    title = "同学"
elif age < 60:
    title = "先生/女士"
else:
    title = "前辈"

print(f"""
================================
👋 你好，{name} {title}！
🎂 你今年 {age} 岁。
🌟 欢迎使用我们的 AI 系统！
================================
""")