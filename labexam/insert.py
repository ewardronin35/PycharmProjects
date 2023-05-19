li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# starts looping
while True:
    # input
    number = input("Enter a number to append in the list: ")

    # appends
    add = li.insert(int(number))

    # appends number
    if li.count(add) == 0:
        print("You have append " + number + " In the list")
        print(li)
    else:
        print("You didn't enter in the list")
        print(li)