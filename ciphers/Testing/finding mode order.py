print("How man numbers in your list?")
numbers = int(input())
listNumbers = []
for number in range(0,numbers):
    print("Which number to add?")
    number = int(input())
    listNumbers.append(number)
    print("--------")
print(listNumbers)
    
from collections import Counter
data = Counter(listNumbers)
print(data)
print(data.most_common())# Returns all unique items and their counts
print(data.most_common(1))  # Returns the highest occurring item
for number in data:
    print (number)
for number in data.most_common():
    print (number)


if data.most_common(1) == 4:
    print("yes")
else:
    print("no")
