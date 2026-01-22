import random
print("========Task 1========")
print("========Subtask 1========")
a = input().split()
half=len(a)//2
print(*a[half:])
print("========Subtask 2========")
a = input().split()
n=len(a)
for i in range(0,n):
    if int(a[i])%2==0:
        print(a[i],end=" ")
print("\n========Subtask 3========")
a=input().split()
a=[int(x) for x in a]
n=len(a)
count = 0
for i in range (1,n-1):
   if a[i]>a[i-1] and a[i]>a[i+1]:
        count +=1
print(count)    
print("\n========Subtask 4========")
a=input().split()
a=[int(x) for x in a]
n=len(a)
middle=sum(a)/len(a)
MoreThanAverage=0
print(middle)
for i in range (0,n):
    if a[i]>middle:
        MoreThanAverage+=1
print(MoreThanAverage)
print("\n========Subtask 5========")
a=input().split()
a=[int(x) for x in a]
n=len(a)
WholeNumber=0
for digit in a:
    WholeNumber=WholeNumber*10+digit
print(WholeNumber)
print("========Task 2========")
a = input("Enter few numbers: ").split()
a = [int(i) for i in a]
result=0
for i in range(len(a)):
    result +=a[i]
print("Sum of numbers:", result)

print("\n-------- Task 2.2 --------")
arr = [random.randint(-50, 50) for _ in range(21)]
print("Array:", arr)
positives = [x for x in arr if x > 0]
print("Positive elements (in order):", positives)
if len(positives) >= 6:
    product = positives[1] * positives[3] * positives[5]  
    print("Product of 2nd, 4th and 6th positive elements:", product)
else:
    print("Not enough positive elements to compute the product (need at least 6).")
print("\n-------- Task 2.3 --------")
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kiev', 'Hong Kong']
message = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print("Formatted message:", message)
longest_city = max(cities, key=len)
print("City with the largest length:", longest_city, "(length:", len(longest_city), ")")
print("\n-------- Task 2.4 --------")
digits = input("Enter 5 digits separated by spaces: ").split()
if len(digits) != 5:
    print("Expected exactly 5 items; received", len(digits))
else:
    reversed_digits = digits[::-1]
    number = int(''.join(reversed_digits))
    print("Reversed list:", reversed_digits)
    print("Number formed by reversed list:", number)
print("\n-------- Task 2.5 --------")
xy_input = input("Enter two values for x and y separated by space: ").split()
if len(xy_input) != 2:
    print("Expected exactly 2 values; received", len(xy_input))
else:
    x, y = xy_input[0], xy_input[1]
    print("Before swap: x =", x, ", y =", y)
    x, y = y, x 
    print("After swap:  x =", x, ", y =", y)
print("========Task 3========")
months =["January", "February", "March", "April", "May", "June"," July", "August", "September", "October", "November", "December"]
for x in range (0,len(months),2):
    print(months[x])

print("========Task 4========")
queens = []

for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

attack = False

for i in range(8):
    for j in range(i + 1, 8):
        x1, y1 = queens[i]
        x2, y2 = queens[j]

        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            attack = True

if attack:
    print("YES")
else:
    print("NO")
