from Lab7_functions import Welcoming_Message,Words_connector,Key_Power_Value,Connect_Strings,Min_and_Max
from Lab10_task4 import *

name=input("Enter your name: ")
Welcoming_Message(name)
string1=input("Enter first word: ")
string2=input("Enter second word: ")
print(Words_connector(string1,string2))
numbers=list(map(int,input("Enter some numbers: ").split()))
print(Min_and_Max(numbers))
digit=int(input("Enter a digit: "))
Key_Power_Value(digit)
strings=input("Enter some strings: ").split()
print(Connect_Strings(*strings))
numbers = [random.randint(1, 1100) for _ in range(100)]
print("Count of even numbers:", Even_num_count_list(numbers))
string_list = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) for _ in range(10)]
print("Random strings:", string_list)
print("Vowels count:", vowels_count_list(string_list))