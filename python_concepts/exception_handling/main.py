# Exception handling block
print("\nException handling block will start")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except Exception:
    print("Error: Invalid input! Please enter a valid number.")
else:
    print("Division was successful!")
finally:
    print("Thank you for using the program.")

print("Exception handling block has ended")

# Custom exception class
class InvalidAgeError(Exception):
    """Raised when the input age is not valid."""
    pass


def check_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be between 0 and 120.")
    return f"Age {age} is valid."


try:
    age_input = int(input("Enter your age: "))
    print(check_age(age_input))
except InvalidAgeError as e:
    print(e)