print("========Task 1========")
print("========Subtask 1========")
a=input()
Upper=a.upper()
print(Upper)

print("========Subtask 2========")
a=input("Enter a string: ")
n=input("Enter a latter: ")
found = 0
for i in range (len(a)):
    if a[i]==n:
        print (i+1)
        found +=1
        break
if found==0:
    print("0")

print("========Subtask 3========")
a=input("Enter a string: ")
a=a.lower()
reverse_a=a[::-1]
if a==reverse_a:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

print("========Subtask 4========")
a=input()
result = ""
for char in a:
    if not char.isdigit():
        result += char
print(result)
result = ""
print("========Subtask 5========")
input_pass=input("Enter your password: ")
for char in input_pass:
   digit=int(char)

   if digit > 5:
       digit= digit //2
       if digit % 2 !=0:
         result += str(digit) 
print("Two step verification code is: ", result)

print("========Task 2========")
char_input=input("Enter a character: ")
print(char_input[2])
print(char_input[-2])
print(char_input[0:5])
print(char_input[::2])
print(char_input[1::2])
print(char_input[::-1])
print(char_input[::-2])
print(len(char_input))

print("========Task 3========")
a=input("Enter a string: ")
word_count=a.count(' ')+1
print("Number of words in the string:", word_count)
