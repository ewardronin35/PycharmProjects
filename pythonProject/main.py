li = [1,2,3,4,6]
# list

# loop
while True:

    # input
    inp = input("Please input a number to the list: ")

    # insert
    li.insert(4,int(inp))

    # print added the new item list
    if li.count(inp) == 0:
        print("The number" + inp + "is added in the list")
        print(li)

    else:
        print("/n failed")