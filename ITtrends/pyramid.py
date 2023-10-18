input_string = "TXL1V9"
numbers_sum = current_number = 0

for char in input_string:
    if '0' <= char <= '9':
        current_number = current_number * 10 + int(char)
    elif current_number > 0:
        numbers_sum += current_number
        current_number = 0

if current_number > 0: numbers_sum += current_number

print(numbers_sum)

# Input a single number
num = int(input("Enter a single number: "))

# Separate the number into two digits
digit1 = num // 10
digit2 = num % 10

# Add the two digits together
result = digit1 + digit2

# Display the result
print("Result:", result)

n = 5  # You can change this to the desired height of the pyramid

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
