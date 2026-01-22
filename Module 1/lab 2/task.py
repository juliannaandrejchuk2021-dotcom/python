from re import match


print("========Task 1========")
print("========Subtask 1========")
correct_pass="secret"
user_input=input("Enter the password: ")
if user_input==correct_pass:
    print("Access granted")
else:
    print("Sorry, that is the wrong password.")
    print("========Subtask 2========")
m1=float(input("Enter mass: "))
V1=float(input("Enter volume: "))
m2=float(input("Enter mass: "))
V2=float(input("Enter volume: "))
p1=m1/V1
p2=m2/V2
if p1>p2:
    print("Object 1 has a greater density.")
else:
    print("Object 2 has a greater density.")
print("========Subtask 3========")
v=float(input("Enter speed in km/s: "))
if v<0:
    print("Invalid speed.")
if v<7.8:
    print("The object will fall back to Earth.")
elif 7.8<=v<11.2:
    print("The object will enter a stable orbit around Earth.")
elif v>=11.2:
    print("The object will escape Earth's gravity.")
elif v>16.7:
    print("The object will escape the Solar System.")

print("========Subtask 4========")
a=int(input("Enter a number between 1 and 10: "))
if 0<a<4:
    print(("I"*a))
elif a==4:
    print("IV")
elif a==5:
    print("V")
elif 6<=a<=8:
    print("V"+"I"*(a-5))
elif a==9:
    print("IX")
elif a==10:
    print("X")
else:
    print("Number out of range.")
print("========Subtask 5========")
school_mark=int(input("Enter your mark (0-12): "))
match
if 0<school_mark<=4:
    print("initial lever")
elif 5<=school_mark<=7:
    print("average level")
elif 8<=school_mark<=10:
    print("sufficient level")
elif school_mark==12 or school_mark == 11:
    print("high level")
else:
    print("Wrong mark entered.")
print("========Task 2========")
a=int(input("Enter a year: "))
if (a%4==0 and a%100!=0) or (a%400==0):
    print(f"{a} is a leap year.")
else:
    print(f"{a} is not a leap year.")
  
