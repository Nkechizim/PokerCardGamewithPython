candy_bars = {"Milky Way", "Bounty", "Snickers"}
sweet_things = {"Muffins", "Snickers", "Candy Floss"}

#the union method returns a new set by merging both sets and removing duplicates 
print(candy_bars.union(sweet_things))
print(sweet_things | candy_bars)

values = {1, 5, 7, 8, 6, 9}
values2 = {1.0, 7.0, 6.5, 8.9}
print(values2.union(values))
print(values | values2)