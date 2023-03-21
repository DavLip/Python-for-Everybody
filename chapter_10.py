"""
Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
Count the number of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

input_file = input("What is the file name: ")
try:
    fname = open(input_file)
except:
    print("File not found")
    exit()
    
emails = dict()
lst = list()
for line in fname:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    else:
        lst = line.split()
        if lst[1] not in emails:
            emails[lst[1]] = 1
        else:
            emails[lst[1]] += 1


# Sort the dictionary by value
lst = list()
for key, val in emails.items():
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)



"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

input_file = input("What is the file name: ")
try:
    fname = open(input_file)
except:
    print("File not found")
    exit()
    
emails = dict()
lst = list()
hours = list()
hours_dict = dict()
for line in fname:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    else:
        lst = line.split()
        if len(lst)>2:
            hours = lst[5].split(':')
            if hours[0] not in hours_dict:
                hours_dict[hours[0]] = 1
            else:
                hours_dict[hours[0]] += 1


# Sort the dictionary by value
lst = list()
for key, val in hours_dict.items():
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)


"""
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
Your program should convert all the input to lower case and only count the letters a-z. 
Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
Find text samples from several different languages and see how letter frequency varies between languages. 
Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

input_file = input("What is the file name: ")
try:
    fname = open(input_file)
except:
    print("File not found")
    exit()
    
counts = dict()
for line in fname:
    line = list(line.rstrip())
    for letter in line:
        if not letter.isalpha():
            continue
        else:
            letter = letter.lower()
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1
            
print(counts)
# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append((val, key))

print(lst)

lst.sort(reverse = True)

for val, key in lst:
    print(key, val)