mydict = {}

matrix = int(input("Matrix size: "))

for x in range(matrix):
    values = input(f"Shopping item {x+1}: ")
    mydict[x] = values  # key and value
print(f"You have {x+1} items in the cart")

def change(mydict):
    key = int(input("\nEnter key to search: "))
    value = mydict.get(key) # retrieve value
    if value:
        print(f"Found {value} item") 
        newValue = input("Enter value: ").lower()
        mydict[key] = newValue
    else:
        print("I'm sorry, not in the cart")

def display(mydict):
    print("\nDisplaying Values")
    print("{:<10} {:<15}".format("Key", "Value"))
    for key, value in mydict.items():
        print("{:<10} {:<15}".format(key, value))

def remove(mydict):
    key = int(input("\nEnter key to delete: "))
    value = mydict.get(key) # retrieve value
    if value:
       print(f"The key {key} with value {value} has been deleted")
       del mydict[key]
    else:
        print("Key not found")
        
def search(mydict):
    # choice = input("Search by item or key? ")
    # if choice == "item":
    item = input("\nEnter item to search: ").lower()
    if item in mydict.values():
        print(f"Found {item} item")
    else:
        print("I'm sorry, not in the cart")

    # elif choice == "key":
    key = int(input("\nEnter key to search: "))
    value = mydict.get(key) # retrieve value
    if value:
        print(f"Found {value} item")
    else:
        print("I'm sorry, not in the cart")

while True:
    print("\nWhat would you like to do [C]hange items [R]emove [D]isplay  S[earch]?")
    action = input().lower()

    if action == "c":
        change(mydict)
    elif action == "r":
        remove(mydict)
    elif action == "d":
        display(mydict)
    elif action == "s":
        search(mydict)
    elif action == "*":
        print("Bye")
        break
    else:
        print("Invalid!")