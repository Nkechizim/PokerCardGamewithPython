candy_bars = {"Milky Way", "Bounty", "Snickers"}
sweet_things = {"Muffins", "Snickers", "Candy Floss"}

#tis method returns a new set with only elements that are not shared between the two sets
print(candy_bars.symmetric_difference(sweet_things))
print(candy_bars ^ sweet_things)

values = {1, 5, 7, 8, 6, 9}
values2 = {1.0, 7.0, 6.5, 8.9}
print(values2.symmetric_difference(values))
print(values2 ^ values)