"""
华氏温度 (Fahrenheit) 和 摄氏温度 (Celsius) 互换
Fahrenheit and Celsius Temperature Converter
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """摄氏度 -> 华氏度: F = C × 9/5 + 32"""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """华氏度 -> 摄氏度: C = (F - 32) × 5/9"""
    return (fahrenheit - 32) * 5 / 9


def main():
    print("=" * 40)
    print("  温度转换器 Temperature Converter")
    print("=" * 40)
    print("1. 摄氏度 → 华氏度 (Celsius → Fahrenheit)")
    print("2. 华氏度 → 摄氏度 (Fahrenheit → Celsius)")
    print("3. 退出 (Quit)")
    print("=" * 40)

    while True:
        choice = input("\n请选择 / Choose (1/2/3): ").strip()

        if choice == "3":
            print("再见! Goodbye!")
            break

        if choice not in ("1", "2"):
            print("无效输入，请重试。Invalid choice, try again.")
            continue

        try:
            value = float(input("请输入温度 / Enter temperature: ").strip())
        except ValueError:
            print("请输入一个有效数字。Please enter a valid number.")
            continue

        if choice == "1":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C = {result:.2f}°F")
        else:
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F = {result:.2f}°C")


if __name__ == "__main__":
    # 简单的演示 / Quick demo
    print("演示 Demo:")
    print(f"  0°C   = {celsius_to_fahrenheit(0):.2f}°F")
    print(f"  100°C = {celsius_to_fahrenheit(100):.2f}°F")
    print(f"  32°F  = {fahrenheit_to_celsius(32):.2f}°C")
    print(f"  212°F = {fahrenheit_to_celsius(212):.2f}°C")
    print()
    main()
