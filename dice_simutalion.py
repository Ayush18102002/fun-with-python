import random

target =  100
score = 0
attempt = 0


while attempt < 20:
    input("To roll the dice press ENTER....")
    dice = random.randint(1,6)
    score += dice
    attempt += 1


    print("you rolled:", dice)
    print("your score:", score)
    print("your attempt:",attempt)
    print(" ------------------------------")

    if score >= target:
        print("YOU WON!!!!")
        break
else:
    print("YOU LOST!!!")
