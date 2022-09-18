candy_bars = {"Milky Way", "Bounty", "Snickers"}
sweet_things = {"Muffins", "Snickers", "Candy Floss"}

# the intersection method returns a new set with only elements that can be found in both sets
print(candy_bars.intersection(sweet_things))
print(candy_bars & sweet_things)
print(candy_bars)
print(sweet_things)

print()

values = {1, 5, 7, 8, 6, 9}
values2 = {1.0, 7.0, 6.5, 8.9}

print(values2.intersection(values))
print(values2 & values)