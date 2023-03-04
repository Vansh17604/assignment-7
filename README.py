# assignment-7
# Function to calculate factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

# Get input from user
num = int(input("Enter a number: "))

# Call the factorial function and print the result
print("Factorial of", num, "is", factorial(num))
