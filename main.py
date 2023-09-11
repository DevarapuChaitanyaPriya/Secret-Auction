from art import logo
import os

print(logo)
print("Welcome to secret auction program.")
d = {}
flag = True
while (flag):
    name = input('What is your name?:').rstrip()
    bid = int(input("what's your bid? $"))
    d[name] = bid
    again = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower().rstrip()
    if (again == "yes"):
        os.system('clear')
    else:
        flag = False
l = list(d.values())
highest_bid = l.index(max(l))
l1 = list(d.keys())
person_name = l1[highest_bid]
print(f"The winner is {person_name} with a bid of ${max(l)}")
