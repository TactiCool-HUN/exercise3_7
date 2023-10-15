# starting input
# this is probably over-engineering in this type of project,
# but sometimes it IS important to have very safe inputs


def parcel_calculator():
    while True:
        is_letter = input("Letter or Parcel?\n").lower()
        if is_letter == "letter" or is_letter == "l":
            is_letter = True
            break
        elif is_letter == "parcel" or is_letter == "p":
            is_letter = False
            break
        else:
            print('Please only input "letter" or "parcel".')

    while True:
        weight = input(f"Weight of packet? (grams)\n")
        if weight.isnumeric():
            weight = float(weight)
            break
        else:
            print("Please only enter a numeric value. Use dot for decimal numbers.")

    # main calculations
    if is_letter:
        cost = 0.5

        if weight > 500:
            cost = cost + 0.07 * (weight // 100)

            # asking if it's too large and adding if yes
            while True:
                fits_box = input("Does it fit the fits_box? (y/n)\n").lower()
                if fits_box == "y" or fits_box == "yes":
                    break
                elif fits_box == "n" or fits_box == "no":
                    cost += 2
                    break
                else:
                    print('Please only enter the letter "y" or the letter "n".')
        elif weight > 200:
            cost = cost + 0.04 * (weight // 100)
    else:  # aka it's a parcel
        cost = 2

        if weight > 500:
            cost = cost + 0.14 * (weight // 100)
        elif weight > 200:
            cost = cost + 0.08 * (weight // 100)

    # output
    print(f"The cost is {round(cost, 2)} €")


choice = "y"
while True:
    if choice == "y":
        parcel_calculator()
    else:
        break
    choice = input("Would you like to calculate another parcel? (y/n)").lower()
