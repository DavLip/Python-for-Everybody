"""
Exercise 1: Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""
def chop(list_mod):
    new_list = []
    for i in list_mod[1:len(list_mod)-1]:
        new_list.append(i)
    return new_list


"""
Exercise 4: Find all unique words in a file

Shakespeare used over 20,000 words in his works. 
But how would you determine that? 
How would you produce the list of all the words that Shakespeare used? 
Would you download all his work, read it and track all unique words by hand?

Let’s use Python to achieve that instead. 
List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

To get started, download a copy of the file www.py4e.com/code3/romeo.txt. 
Create a list of unique words, which will contain the final result. 
Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function. 
For each word, check to see if the word is already in the list of unique words. 
If the word is not in the list of unique words, add it to the list. 
When the program completes, sort and print the list of unique words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']

"""
fhandle = open("romeo.txt")
unique_list = []
for line in fhandle:
    word_list = line.split()
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
        continue

unique_list.sort()
print(unique_list)

"""
Exercise 5: Minimalist Email Client.

MBOX (mail box) is a popular file format to store and share a collection of emails. 
This was used by early email servers and desktop apps. 
Without getting into too many details, MBOX is a text file, which stores emails consecutively. 
Emails are separated by a special line which starts with From (notice the space). 
Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. 
Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. 
We are interested in who sent the message, which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end. 
This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word

"""
input_data = input("Enter a file name:")
try:
    fhandle = open(input_data)
    email_count = 0
    for line in fhandle:
        if not line.startswith("From "):
            continue
        line_split = line.split()
        print(line_split[1])
        email_count = email_count + 1
    print("There were", email_count, "lines in the file with From as the first word", sep=" ")
except:
    print("File not found")

"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0

"""

numbers_list = []
while True:
    input_numbers = input("Enter a number: ")
    if input_numbers != "done":
        numbers_list.append(float(input_numbers))
    else:
        break

print("Maximum: ", max(numbers_list))
print("Minimum: ", min(numbers_list))