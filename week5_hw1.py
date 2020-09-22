'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
di = dict()
word = list()
name = input("Enter file:")
if len(name) > 1 : 
    handle = open("mbox-short.txt")
    for line in handle :
        if line.startswith("From ") :
            word = line.split()
            if word[1] in di.keys():
                di[word[1]] = di[word[1]] + 1
            else:
                di[word[1]] = 1
            

largest = -1
theword = None
for k, v in di.items() :
    if v > largest :
        largest = v
        theword = k

print(theword, largest)
