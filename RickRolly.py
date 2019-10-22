import random
my_list = ["shorturl.at/dhoOZ", "shorturl.at/gpzL2", "shorturl.at/jn048", "shorturl.at/hxR56", "shorturl.at/zGP39", "shorturl.at/suS27", "shorturl.at/zCKQ2", "shorturl.at/bhw28", "shorturl.at/lnxAI", "shorturl.at/apD01"]
print(random.choice(my_list))
tries = 1

while True:
    action = str(input("Were you just rickroll\'d?: "))
    if action == "yes":
        print("You Lose")
        break
    else:
        print(random.choice(my_list))
        tries += 1
    if tries > 3:
        print("Congratulations! You Won!")
        break

