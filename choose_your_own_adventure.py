name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ").lower()

if answer == "left":
    answer = input(
        "You have come to a river, you can walk around or swim across? Type walk to walk or swim to swim across")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You died.")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input(
        "You have come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ")

    if answer == "back":
        print("You go back and are eaten alive by coyotes.")
    elif answer == "cross":
        print(
            "You cross the brideg and meet a stranger. Dou you talk to them? (yes/no ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose!")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")


print("Thank you for trying", name)
