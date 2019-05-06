"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_spent = {}
for call in calls:
    time_spent[call[0]] = time_spent.get(call[0], 0) + int(call[3])
    if call[0] != call[1]:
        time_spent[call[1]] = time_spent.get(call[1], 0) + int(call[3])

longest_number = None
for number,seconds in time_spent.items():
    if longest_number is None or seconds > time_spent[longest_number]:
        longest_number = number
print("{} spent the longest time, {} seconds, on the phone during Sptember 2016.".format(longest_number, time_spent[longest_number]))
