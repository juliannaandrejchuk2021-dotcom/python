print("=========Task 1=========")
def even_months(months):
    return [months[i] for i in range(0, len(months), 2)]
def unique_elements(elements):
    return list(set(elements))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("Even indexed months:", even_months(months))
elements = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", unique_elements(elements))
print("=========Task 2=========")
import random
def isDigits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def main():
    for _ in range(10):
        num = random.randint(1, 50000)
        print(num, "-> digits:", isDigits(num))
main()    
print("=========Task 3==========")
def F1(string):
    result = ""
    for i in range(len(string)):
        char=string[i]
        if ord('a') <= ord(char) <=ord('z'):
            result = char + result
    return result

string=input("Enter a string: ")
print("Result:", F1(string))
