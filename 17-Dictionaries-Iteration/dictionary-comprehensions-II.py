chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Rib": 7.99,
    "Fried Rice": 1.99
}

invert = {value: key for key, value in chinese_food.items()}
print(invert)

def coaster_conversion(diction):
    feet= {key: round(value*3.28084) for key, value in diction.items()}
    return feet

coasters = {
    "Kingda Ka": 139,
    "Top Thrill Dragster": 130,
    "Superman: Escape From Krypton": 126
}

print(coaster_conversion(coasters))