import random
emoji={"r":"🪨","p":"📃","s":"✂️"}
choices=["r","p","s"]
while True:
    user_choice=input("rock,paper or scissors (r/p/s): ").lower()
    if user_choice not in choices:
        print("invalid choice")
        continue
    computer_choice=random.choice(choices)

    print(f"you choose {emoji[user_choice]}")
    print(f"computer choice {emoji[computer_choice]}")

    if user_choice==computer_choice:
        print("tie")
    elif \
        (user_choice=="r" and computer_choice=="s") or \
        (user_choice=="s" and computer_choice=="p")or \
        (user_choice=="p" and computer_choice=="r"):
        print("you won")
    else:
        print("you lose")
    should_continue=input("continue?(y/n): ").lower()
    if should_continue=="y":
        continue
    else:
        print("thank you!!")
        break



