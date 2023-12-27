import random as rd
max=100
min=0
num=rd.randint(min,max)
time=7
n=0
print("You have 3 times to guess the number")
for i in range(0,time):
    n+=1
    print(f"The range is between {min} to {max}")
    guess=int(input(("please input a number: ")))
    if guess>max or guess<min:
        guess=int(input(("Exceed the range, please input again:")))
    print("your guess number is: ",guess)
    if guess==num:
        print("Congratulations! You're right!")
        break
    elif guess<num:
        min=guess
        print("Pity! You're wrong, remaining ",time-n,"times")
    else:
        max=guess
        print("Pity! You're wrong, remaining ",time-n,"times")
if time-n==0 and guess!=num:
    print("You lose!")
        
