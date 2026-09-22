num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = int(num1) * int(num2)
print(num1 + " × " + num2 + " = " + str(result))

if (result > 0):
    print("The result is positive.")
if (result < 0):
    print("The result is negative.")
if (result == 0):
    print("The result is positive and negative.")