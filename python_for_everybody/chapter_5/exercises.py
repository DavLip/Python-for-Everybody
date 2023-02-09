""" Write a program which repeatedly reads numbers until the user enters “done”. 
    Once “done” is entered, print out the total, count, and average of the numbers. 
    If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number."""

numbers = []
while True:
    numbers_input = input("> ")
    if numbers_input == "done":
        break
    try:
        numbers_input = int(numbers_input)
        print("Enter a number:", numbers_input)
        numbers.append(numbers_input)
    except:
        print("Invalid input")
        
print(sum(numbers), len(numbers), sum(numbers)/len(numbers))
