import sys

phoneBook = {"Cait" : 3160495066, "Mairi" : 5806546770, "Lorna" : 4091163363, "David" : 2052676643, "Zoe" : 8012615156, }

noExit = True

print(" ")
print("Welcome to Phone Book Search", '\n')
def start():
    name = input("Please enter a name or type exit to exit: ",)

    if name == "exit":
        sys.exit()
    else:
        if name in phoneBook:
            print('\n', name, ": ", phoneBook[name], '\n')
        else:
            print('\n' "There is no record of a phone number under the name: ", name, '\n')

while noExit:
    start()
