import random

START_BAL = 500

REDSET = { 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3 }
BLACKSET = { 15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26 }

balance = START_BAL
playing = True
while playing:
    print("Balance:", balance)
    print("Make a bet")
    print("Eg. 50 red, 5 even, 1 3")
    bets = input("> ").split(", ")
    number = random.randint(0,37)

    for bet in bets:
        wager, placement = bet.split(" ")
        wager = int(wager)
        condition = False
        if placement.isnumeric():
            balance += 35 * wager if number == placement else -wager
        else:
            match placement:
                case "red":
                    balance += wager if number in REDSET else -wager
                case "black":
                    balance += wager if number in BLACKSET else -wager
                case "even":
                    balance += wager if number % 2 == 0 else -wager
                case "odd":
                    balance += wager if number % 2 == 1 else -wager
                case "lowerhalf":
                    balance += wager if number <= 18 else -wager
                case "upperhalf":
                    balance += wager if number >= 19 else -wager
                case _:
                    print("unknown bet")
    print("Number:", number, "(red)" if number in REDSET else "")
    print()
