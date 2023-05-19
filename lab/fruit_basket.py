from collections import deque


# Create an empty stack

basket = deque()

# Prompt the user to input the number oof fruits to catch

num_fruits = int(input("Enter the number of fruits you want to catch: "))

# Loop through the number of fruits and prompt the user to choose a fruit to catch
for i in range(num_fruits):
    fruit_choice = input(f"Choose a fruit to catch ({i+1}/{num_fruits}) (A- Apple, O- Orange, M - Mango, G - Guava): ").upper()
    if fruit_choice == "A":
        basket.append("apple")
    elif fruit_choice == "O":
        basket.append("orange")
    elif fruit_choice == "M":
        basket.append("Mango")
    elif fruit_choice == "G":
        basket.append("guava")
    else:
        print("Invalid fruit choice")
        i -= 1

# Display all the fruits in the basket
print("The basket has:", basket)

# Prompt the user to start eating a fruit
while input("Press E to start eating the Fruit: ").upper() == "E":
    if basket:
        eaten_fruit = basket.pop()
        print(f"You eat a {eaten_fruit}. Snacks remaining: {len(basket)}")
    else:
        print("No more fruit")
        break