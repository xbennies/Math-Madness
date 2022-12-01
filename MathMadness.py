import time
import random

def quiz():
    global score
    operators = ['+', '-']
    sum1 = random.randint(1,10)
    sum2 = random.choice(operators)
    sum3 = random.randint(1,10)
    question = 0
    answer = 0
    if sum2 == '+':
        question = sum1 + sum3
    elif sum2 == '-':
        question = sum1 - sum3
    answer = input("What is " + str(sum1) + " " + sum2 + " " + str(sum3) + "? ")
    if int(answer) == question:
        score += 1
        print("Correct!")
    else:
        print("Wrong! The answer was " + str(question))

score = 0

print("Welcome to Math Madness!")
time.sleep(1)
print("You are currently running a pre-release build. Expect bugs/issues/crashes when using this software.")
time.sleep(1)
print("Math Madness is a basic maths quiz running in Python. Ready to give it a try? Try and beat all 10 randomly-generated questions!")
time.sleep(2)
print("Ready?")
time.sleep(0.75)
print("Set?")
time.sleep(0.75)
print("Go!!!")
time.sleep(0.25)

for math in range(0,10):
    quiz()

print("Nice! You answered all 10 questions! Out of them 10, you got " + str(score) + " correct. Well done!")