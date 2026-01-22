import os
import time
import random
import datetime
import math
import sys
import csv
from random import randint
BASE_DIR = os.path.dirname(__file__)
#1
#1.1
print(sys.version)
#1.2
n=int(input("Enter a number: "))
print(math.factorial(n))
#1.3
string=input("Enter a string: ").split()
random.shuffle(string)
print(f"Shuflled string: {string} ")
#1.4
count=0
input_path=os.path.join(BASE_DIR, 'input.txt')
with open(input_path, 'r', encoding='utf-8') as file:
    for _ in file:
        count+=1
    
print(f"Number of lines in the file: {count}")
#1.5
print(f"""
Current date and time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Current year: {datetime.datetime.now().year}
Month of the year: {datetime.datetime.now().month}
Week number of the year: {datetime.datetime.now().isocalendar()[1]}
Weekday of the week: {datetime.datetime.now().isocalendar()[2]}
Day of the year: {datetime.datetime.now().timetuple().tm_yday}
Day of the month: {datetime.datetime.now().day}
Day of the week: {datetime.datetime.now().weekday()}
""")
#2


numbers_path = os.path.join(BASE_DIR, 'numbers.txt')
sum_path = os.path.join(BASE_DIR, 'sum_numbers.txt')

with open(numbers_path, 'r') as numbers:
    list_of_numbers = [int(i) for i in numbers]

print(sum(list_of_numbers))

with open(sum_path, 'w') as output_file:
    output_file.write(str(sum(list_of_numbers)))
text_path = os.path.join(BASE_DIR, 'text.txt')
empty_path = os.path.join(BASE_DIR, 'empty.txt')

with open(text_path, 'r') as source_file:
    text = source_file.read()

with open(empty_path, 'w') as target_file:
    target_file.write(text)

with open(empty_path, 'r') as target_file:
    copied = target_file.read()

print("Content of second file:", copied)
os.remove(text_path)
#3

with open('random_numbers.txt', 'w') as new_file:
    new_file.write(str([randint(-1000,1000) for i in range(150)]))

with open('random_numbers.txt', 'r') as target_file:
    random_numbers = target_file.read()

random_numbers = random_numbers[1:-2]
list1 = list(map(int, random_numbers.split(', ')))
sorted_list = sorted(list1)

with open('random_numbers.txt', 'w') as target_file:
    target_file.truncate()
    target_file.write(str(sorted_list))

#4

painters_data = '''author, canvas
Vincent Willem van Gogh, "Vase with sunflowers"
Rembrandt Harmenszoon van Rijn, "Aristotle"
Leonardo da Vinci, "Self-portrait"
'''

with open('painters.csv', 'w') as target_file:
    target_file.write(painters_data)

with open('painters.csv', 'r') as source_file:
    painters = list(csv.DictReader(source_file))
    for i in painters:
        print(f"Author: {i['author']}, Canvas: {i[' canvas']}")
    print()

imdb = [
{
'title': 'Lord of the Rings: Two towers',
'year': 2002,
'rating': 8.7
},
{
'title': 'Matrix',
'year': 1999,
'rating': 8.7
},
{
'title': 'Interstellar',
'year': 2014,
'rating': 8.5
},
{
'title': 'Back to the Future',
'year': 1985,
'rating': 8.5
},
{
'title': 'Logan: Wolverine',
'year': 2017,
'rating': 8.1
}
]

with open('imdb.csv', 'w', newline='') as new_file:
    fieldnames = ['title', 'year', 'rating']
    writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(imdb)

with open('imdb.csv', 'r') as target_file:
    reader = csv.DictReader(target_file)
    for i in reader:
        print(f"Movie: {i['title']}, Year: {i['year']}, Rating: {i['rating']}")
    print()

current_dir = os.getcwd()
print(current_dir)
files = os.listdir(current_dir)
for i in files:
    print(f"  - {i}")

file_size = os.path.getsize('painters.csv')
print(f"painters.csv size: {file_size} bytes")
print()

for i in os.listdir('.'):
    if i.endswith('.csv'):
        print(f"  - {i}")