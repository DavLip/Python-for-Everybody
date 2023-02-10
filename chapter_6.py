"""
Exercise 1: Write a while loop that starts at the last character in the string and 
works its way backwards to the first character in the string, printing each letter 
on a separate line, except backwards.
"""
itevar = 0
fruit = 'apple'
while itevar < len(fruit):
    reverse_fruit = fruit[::-1]
    print(reverse_fruit[itevar])
    itevar = itevar + 1