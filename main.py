is_letter = input("Letter or Parcel?\n").lower() == "letter"
weight = float(input(f"Weight of packet? (grams)\n"))
cost = mailbox = 0
if weight > 500:
    cost = 0.14 * (weight // 100)
    if is_letter:
        mailbox = input("Does it fit the mailbox? (y/n)\n").lower() == "n"
elif weight > 200:
    cost = 0.08 * (weight // 100)
print(f"The price is {round(2 / (int(is_letter) * 3 + 1) + cost / (int(is_letter) + 1) + 2 * int(mailbox), 2)} €")
