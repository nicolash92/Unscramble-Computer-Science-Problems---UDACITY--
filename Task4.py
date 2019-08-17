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
non_telemarketer_numbers = set()
possible_telemarketer_numbers = set()

for text in texts:
    non_telemarketer_numbers.add(text[0])
    non_telemarketer_numbers.add(text[1])
for call in calls:
    non_telemarketer_numbers.add(call[1])

for call in calls:
    if not call[0] in non_telemarketer_numbers:
        possible_telemarketer_numbers.add(call[0])

possible_telemarketer_numbers = list(possible_telemarketer_numbers)
possible_telemarketer_numbers.sort()

print('These numbers could be telemarketers: ')
for number in possible_telemarketer_numbers:
    print(number)
