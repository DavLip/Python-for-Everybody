"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt

Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""
input_file = input("What is the file name: ")
try:
    fhandle = open(input_file)
except:
    print("File not found")
    exit()

words_dict = dict()

for line in fhandle:
    line = line.rstrip().split()
    for word in line:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

for key, val in words_dict.items():
    print(key, val, sep = " ")
    


"""
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:

python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

fname = input("What is the file name: ")
try:
    fname = open(fname)
except:
    print("File not found: ", fname)
    exit()

days = dict()  
for line in fname:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    else:
        if not len(line.split()) == 7:
            continue
        else:
            if line.split()[2] not in days:
                days[line.split()[2]] = 1
            else:
                days[line.split()[2]] += 1

print(days)

lst = list(days.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, days[key])

"""
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""

fname = input("What is the file name: ")
try:
    fname = open(fname)
except:
    print("File not found: ", fname)
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


sorted_values = sorted(emails.values()) # Sort the values
print(type(sorted_values))
sorted_dict = {}

for i in sorted_values:
    for k in emails.keys():
        if emails[k] == i:
            sorted_dict[k] = emails[k]

print(sorted_dict)

"""
Exercise 4: Add code to the above program to figure out who has the most messages in the file. 
After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) 
    to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

fname = input("What is the file name: ")
try:
    fname = open(fname)
except:
    print("File not found: ", fname)
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
            
max_email = max(emails.values())
for key in emails.keys():
    if emails[key] == max_email:
        print(key)

"""
Exercise 5: This program records the domain name (instead of the address) 
    where the message was sent from instead of who the mail came from (i.e., the whole email address). 
At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

fname = input("What is the file name: ")
try:
    fname = open(fname)
except:
    print("File not found: ", fname)
    exit()

domains_count = dict()
lst = list()
email = None
domain = None
for line in fname:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    else:
        lst = line.split()
        email = lst[1]
        idx = email.index("@")
        domain = email[idx+1:]
        if domain not in domains_count:
            domains_count[domain] = 1
        else:
            domains_count[domain] += 1
            
print(domains_count)