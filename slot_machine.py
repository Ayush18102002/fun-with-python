import random

print("---- SLOT MACHINE ----")

symbols = ["🍒", "🍋", "🍊", "🍉", "⭐"]

while True:

    input("To spin, press ENTER ")

    result = [
        random.choice(symbols),
        random.choice(symbols),
        random.choice(symbols)
    ]

    print(" | ".join(result))

    if result[0] == result[1] == result[2]:
        print("JACKPOT!")

    elif (result[0] == result[1] or
          result[1] == result[2] or
          result[0] == result[2]):
        print("OOPS! MATCHED!")

    else:
        print("Try again!")

    more = input("Do you want to spin more? (yes/no): ").lower()

    if more == "no":
        break

print("Thanks for playing!")