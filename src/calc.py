def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a + b  # 故意写错，稍后用 revert 撤销


def divide(a, b):
    """返回 a 除以 b 的浮点结果。"""
    return a / b


def main():
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"8 / 2 = {divide(8, 2)}")


if __name__ == "__main__":
    main()
