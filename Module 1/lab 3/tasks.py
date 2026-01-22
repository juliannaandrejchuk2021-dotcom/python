print("========Task 1========")
print("========Subtask 1========")
n=int(input())
i=0
while i<n:
    print("Hello, World!")
    i+=1

print("========Subtask 2========")
a=int(input())
for i in range(a+1):
    print(f"{i}"* i)

print("========Subtask 3========")
a=int(input())
for i in range(a+1):
    print(f"{i*i}")
  
print("========Subtask 4========")
n=int(input())
if n>=2:
    result_1=0
    for i in range(1,n):
        result_1 += i * (i + 1)
    print(result_1)
else:
    print("Input should be greater than or equal to 2")

print("========Subtask 5========")
n=float(input())
tenmin = 10
for i in range(5):
    print(n*tenmin)
    tenmin += 5

print("========Task 2========")
import random
result=0
n=random.randint(100,999)
print(f"Random number: {n}")
while n>0:
    digit=n%10
    result+=digit
    n=n//10

print(f"Sum of digits: {result}")
print("========Task 3========")
n=int(input())
penguin=["   _~_    ",
         "  (o o)   ",
         " /  V  \\  ",
         "/(  _  )\\ ",
         "  ^^ ^^   "]
if 0<n<10:
    for row in penguin:
        print(row*n)