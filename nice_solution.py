# starting input
is_letter = input("Letter or Parcel?\n").lower()
is_letter = is_letter[0] == "letter"
weight = float(input(f"Weight of packet? (grams)\n"))

# declaring globally needed stuff
fits_box = False

# main calculations
if is_letter:
    cost = 0.5

    if weight > 500:
        cost = cost + 0.07 * (weight // 100)

        # asking if it's too large and adding if yes
        fits_box = input("Does it fit the mailbox? (y/n)\n").lower()
        if fits_box[0] is not "y":
            cost += 2
    elif weight >= 200:
        cost = cost + 0.04 * (weight // 100)
else:  # aka it's a parcel
    cost = 2

    if weight > 500:
        cost = cost + 0.14 * (weight // 100)
    elif weight >= 200:
        cost = cost + 0.08 * (weight // 100)

# output
print(f"The cost is {cost} €")
