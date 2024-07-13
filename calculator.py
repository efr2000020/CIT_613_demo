class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Example usage (commented out to prevent execution during testing)
# if __name__ == "__main__":
#     calc = Calculator()
#     print(calc.add(2, 3))
#     print(calc.subtract(5, 2))
#     print(calc.multiply(3, 4))
#     print(calc.divide(10, 2))
