print("========Task 1========")
print("========Subtask 1========")
dict_Browsers={"Yahoo           !": 2.09, "Google": 90.15, "Bing": 3.23,"Baidu": 2.2}
for key,value in dict_Browsers.items():
    print(f"{key}: {value}")
print("========Subtask 2========"))
print("Enter a number that represents a day in a week:")
WeekDyasDict={
    "Sunday":0,
    "Monday":1,
    "Tuesday":2,
    "Wednesday":3,
    "Thursday":4,
    "Friday":5,
    "Saturday":6
    }

a=int(input())
for value,key in WeekDyasDict.items():
    if a==key:
        print(value)
        break


print("========Subtask 3========")
print("Enter a string:")

b=input()

Letters={
    "Upper":0,
    "Lower":0
}

for ch in b:
    if ch.islower():
        Letters["Lower"] +=1
    elif ch.isupper():
        Letters["Upper"]+=1

for key,value in Letters.items():
    print(f"{key} {value}   ")
print("========Subtask 4========")
print("Enter a letter:")

MorseAplabet={   
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
    }
letters=input()
letters=letters.lower()
if letters in MorseAplabet:
    print(MorseAplabet[letters])

print("========Subtask 5========")
print("Enter 3 cell addresses and their values (e.g., A1 10):")
DataTable={}

for i in range(3):
    addr, value=input().split(maxsplit=1)
    col=addr[0]
    row=addr[1]
    DataTable[(col),(row)]=value

for key in DataTable:
    print(key,DataTable[key])


#2
import random
print("========Task 2========")
U=set(range(1,26))
A=set(random.sample(list(U),12))
B=set(random.sample(list(U),14))
C=set(random.sample(list(U),9))
A_minus=U-A
print(f"A ({len(A)}) =  {sorted(list(A))} ")
print(f"B ({len(B)}) =  {sorted(list(B))} ")
print(f"C ({len(C)}) =  {sorted(list(C))} ")
part1=A-B
part2=A&B
U_result1=A_minus|B-(A&C)
U_result2=part1|part2|C
print(f"Result of variant 1: {sorted(list(U_result1))}")
print(f"Result of variant 19: {sorted(list(U_result2))}")
print(f"Power of variant 1: {len(U_result1)}")
print(f"Power of variant 19: {len(U_result2)}")
#3.1
print("========Task 3.1========")
s = input("Enter few numbers: ")
nums = s.split()
unique_count = len(set(nums))

print("Different numbers count:", unique_count)

#3.2
List_a=[5,7,-1,8,3]
List_b=[8,81,7,-1,9]
print("========Task 3.2========")
print("List A:", List_a)
print("List B:", List_b)

print("Common elements:", sorted(set(List_a) & set(List_b)))
#4
print("========Task 4========")
golossary = {
    "OOP":"Programming paradigm based on objects ",
    "SQL":"Database managment system ",
    "Library" : "Collection of prewritten code that programmers use "
}
for word,defenition in golossary.items():
    print(f"{word}:\t{defenition}")
#5
print("========Task 5======")
ones = {
    1:"one ", 2:"two ", 3:"three ", 4:"four ", 5:"five ",
    6:"six ", 7:"seven ", 8:"eight ", 9:"nine ", 10:"ten ",
    11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
    15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
    19:"nineteen"
}
tens = {
    20:"twenty ", 30:"thirty ", 40:"forty ", 50:"fifty ",
    60:"sixty ", 70:"seventy ", 80:"eighty ", 90:"ninety "
}
def ConvertToWords(n):
    if n==1000:
        return "Onethousand"
    if n>=100:
        hundred_part=ones[n//100]+"hundred "
        if n%100==0:
            return hundred_part
        else:
            return hundred_part+ "and " + ConvertToWords(n%100)
    if n>=20:
        ten_part=tens[(n//10)*10]
        if n%10==0:
            return ten_part
        else:
            return ten_part+ones[n%10]
    return ones[n]
total_letters_used=sum(len(ConvertToWords(i)) for i in range (1,1000+1))
while True:
    n = input("Enter a number (1-1000): ")
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 1000:
            print(ConvertToWords(n))
            break
    print("Invalid input. Try again.")
        

print ("Total latters used from 1 to 1000 ", total_letters_used)
