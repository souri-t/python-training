def fizzbuzz(n: int) -> list[str]:
    """1 から n までの FizzBuzz の結果を配列で返す。"""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    for item in fizzbuzz(20):
        print(item)
