def sum (a : int, b : int) -> int:
    return a + b

def sub (a : int, b : int) -> int:
    return a - b

def mul (a : int, b : int) -> int:
    return a * b

def div (a : int, b : int) -> int:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

if __name__ == "__main__":
    a = 10
    b = 5

    print(f"Sum: {sum(a, b)}")
    print(f"Subtraction: {sub(a, b)}")
    print(f"Multiplication: {mul(a, b)}")
    print(f"Division: {div(a, b)}")