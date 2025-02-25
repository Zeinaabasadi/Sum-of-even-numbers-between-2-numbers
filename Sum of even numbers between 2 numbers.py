num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
x = 0
for i in range (num1, num2+1):
    if i % 2 == 0:
        x += i
    else:
        continue
print(f"the sum of even numbers between {num1} and {num1} is: {x}")
