def celsius_to_fahrenheit(celsius: float) -> float:
    """摂氏を華氏に変換する。"""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """華氏を摂氏に変換する。"""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))   # 212.0
    print(fahrenheit_to_celsius(32))    # 0.0
