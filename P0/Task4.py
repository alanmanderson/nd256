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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

texting_numbers = {}
for text in texts:
    texting_numbers[text[0]] = 1
    texting_numbers[text[1]] = 1

received_calls = {}
sent_calls = {}
for call in calls:
    received_calls[call[1]] = 1
    if call[0] not in texting_numbers:
        sent_calls[call[0]] = 1

potential_telemarketers = []
for number in sent_calls:
    if number not in received_calls:
        potential_telemarketers.append(number)

# It is unclear if we should print the numbers exclusively by the number
# (discounting punctuation).  Here I don't take parenthesis into account
# but because of the format of the numbers it works out anyway

potential_telemarketers.sort()
print("These numbers could be telemarketers: ")
[print(number) for number in potential_telemarketers]

