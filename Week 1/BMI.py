name = input("请输入你的姓名：")
height = float(input("请输入你的身高（cm）："))
weight = float(input("请输入你的体重（kg）："))

# 计算BMI
height_m = height / 100
bmi = weight / (height_m ** 2)
bmi = round(bmi, 1)

# 判断范围
if bmi < 18.5:
    status = "偏瘦 🥗 建议适当增加营养"
elif bmi < 24.9:
    status = "正常 ✅ 继续保持！"
elif bmi < 29.9:
    status = "偏胖 🏃 建议适当运动"
else:
    status = "肥胖 ⚠️ 建议咨询医生"

print(f"""
================================
📊 {name} 的 BMI 报告
--------------------------------
📏 身高：{height} cm
⚖️  体重：{weight} kg
🔢 BMI：{bmi}
💡 状态：{status}
================================
""")
