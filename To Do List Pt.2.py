#Chloe
#1/18
#To-Do List Pt.2

x = ["Sour Patch Kids", "Milk Duds", "Kit Kat", "Twix", "Gummy Bears"]
while True:
    option = int(input("1. Add a task to the to-do list\n2. View the current to-do list\n3. Mark a task as completed \n4. Remove a task from the to-do list\n5. Exit the program"))
    if (option == 1):
        item = input("What would you like to add?")
        x.append(item)
    elif (option == 2):
        print(x)
    elif (option == 3):
        pos = (input("What item do you want to mark complete?"))
        i = x.index(pos)
        x[i] = "✓"
    elif (option == 4):
        y = x.index(input("What item would you like to remove?"))
        x.pop(y)
    elif(option == 5):
        print("cleared all items from list")
        x.clear()
    elif(option == 6):
        print("alphebetizing list now")
        x.sort()
        print(x)
    elif(option == 7):
        y=len(x)
        print(y)
    elif (option == 8):
        print("Program Ended.")
        break
    else:
        print("Invalid Input.")

