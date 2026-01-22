print("=========Task 1=========")
print("=========Subtask 1=========")
def Welcoming_Message(name):
    print(f"Welcome, {name}")

name=input("Enter your name: ")
Welcoming_Message(name)
print("=========Subtask 2=========")
def Words_connector(word1, word2):
    connected_words = word1 + " " + word2
    return connected_words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
result = Words_connector(word1, word2)
print("Connected words:", result)

print("=========Subtask 3=========")
def Min_and_Max(nums):
    return(min(nums), max(nums))
nums=list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Minimum and Maximum:", Min_and_Max(nums))

print("=========Subtask 4=========")
def Key_Power_Value(n):
    d={}
    for i in range(1, n+1):
        d[i] = i**2
    print(d)

n=int(input("Enter a number: "))
Key_Power_Value(n)

print("=========Subtask 5=========")
def Connect_Strings(*args):
    result = ', '.join(args)
    return result
strings = input("Enter strings: ").split()
print("Connected strings:", Connect_Strings(*strings))

print("=========Task 2=========")
def Density(m1,v1,m2,v2):
    p1=m1/v1
    p2=m2/v2
    if p1>p2:
        return "Object 1 has a greater density."
    else:
        return "Object 2 has a greater density."
def Sum_Multiply_Power(a,b,c):
    summ=a+b+c
    multiply=a*b*c
    power_a=a**(b-c)
    return summ, multiply,power_a
def Rome_letter(a):
    if a <5:
        return ("I"*a)
    elif a==5:
        return ("V")
    elif 6<=a<=8:
        return ("V"+"I"*(a-5))
    elif a==9:
        return ("IX")
    elif a==10:
        return ("X")
    else:
        return ("Number out of range.")

print("=========Task 3=========")
def Ten_to_Binary(n):
    if n > 1:
        Ten_to_Binary(n // 2)
    print(n % 2, end='\n')
num= int(input("Enter a decimal number: "))
Ten_to_Binary(num)

print("=========Task 4=========")
def ConvertToList(string):
    return [char for char in string if char !=' ']

def SymbolsCount(string_list):
    result={}
    for char in string_list:
       if char in result:
           result[char]+=1
       else:
           result[char] = 1
    return result
string = input("Enter a string: ")

string_list= ConvertToList (string)
print("String in list format: ",string_list)

symbols=SymbolsCount(string_list)
print("Count of symbols in list: ", symbols)
