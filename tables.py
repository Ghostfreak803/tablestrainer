import random
import time

t_end = time.time() + 60
numbers = list(range(2,20))
numbers.remove(10)
usedcombs = [] # list of used combinations
score = 0
n = 0
while (time.time() < t_end):
    
    # Loop to generate random combinations where at least one value is greater than '10'
    while True:
        x = random.choice(numbers)
        y = random.choice(numbers)
        if (x > 10 or y > 10):
            if {x, y} in usedcombs:
                continue
            else:
                usedcombs.append({x,y})
                break

    myinput = int(input(f"{x} x {y} = ") or "0")

    if myinput == x * y:
        print("Correct!")
        score += 1
    else:
        print("Wrong...")

    n += 1

print(f'Finished! Your score is {score}/{n}')