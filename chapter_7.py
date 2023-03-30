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

"""
Exercise 3: Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments.
"""
def count(word, letter):
    """
    Count the number of times the parameter called "letter" occurs in the parameter "word".
    """
    letter_count = 0
    for itevar in word:
        if itevar == letter:
            letter_count = letter_count + 1
    print('The letter "'
    , letter
    , '" occurs a total of '
    , letter_count
    , ' times in the word '
    ,word
    ,'.'
    , sep='')


"""
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the 
colon character and then use the float function to convert the extracted string 
into a floating point number.
"""

str = 'X-DSPAM-Confidence:0.8475'
colon_idx = str.find(':')
num = float(str[colon_idx + 1:])
print(type(num))

"""
<class 'float'>
"""