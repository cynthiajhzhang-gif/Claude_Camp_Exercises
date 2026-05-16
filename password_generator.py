import random
import string

print("================================")
print("🔐 密码生成器")
print("================================")

while True:
    length_input = input("请输入密码长度（建议8-16位）：")
    if length_input.isdigit():
        length = int(length_input)
        break
    else:
        print("⚠️ 请输入数字！")

print("\n请选择密码类型：")
print("1. 只有数字")
print("2. 只有字母")
print("3. 数字 + 字母")
print("4. 数字 + 字母 + 符号（最安全）")

choice = input("\n请输入选项（1-4）：")

if choice == "1":
    characters = string.digits
elif choice == "2":
    characters = string.ascii_letters
elif choice == "3":
    characters = string.ascii_letters + string.digits
else:
    characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print(f"""
================================
✅ 你的密码已生成！
🔑 密码：{password}
📏 长度：{length} 位
================================
⚠️  请妥善保存，不要告诉别人！
""")