def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Cannot divide by zero"

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Invalid input"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Modulus")
print("7. Floor Divide")
print("8. Square Root")

# Example of adding and finding the square root of two numbers:
print("sum = ", add(4, 6))
print("Square root = ", square_root(8))
