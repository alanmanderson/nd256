"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = {}
for text in texts:
    numbers[text[0]] = 0
    numbers[text[1]] = 0

for call in calls:
    numbers[call[0]] = 0
    numbers[call[1]] = 0

print("There are {} different telephone numbers in the records.".format(len(numbers)))
