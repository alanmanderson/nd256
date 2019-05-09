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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_area_code(number):
    if number.startswith('('):
        paren_index = number.index(')')
        return number[1:paren_index]
    if number[0] in ['7', '8', '9']:
        return number[0:4]
    if number[0:3] == '140':
        return '140'
    raise Exception('Invalid number: ' + number)

bangalore_recipients = {}
bangalore_fixed_recipients = 0
total_calls = 0
for call in calls:
    total_calls += 1
    if call[0].startswith('(080)'):
        area_code = get_area_code(call[1])
        bangalore_recipients[area_code] = None
        if area_code == '080':
            bangalore_fixed_recipients += 1

print("The numbers called by people in Bangalore have codes:")
bangalore_recipients = list(bangalore_recipients.keys())
bangalore_recipients.sort()
[print(code) for code in bangalore_recipients]


percent_local = bangalore_fixed_recipients / total_calls * 100
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent_local, 2)))
