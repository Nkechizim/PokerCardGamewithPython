candy_bars = {"Milky Way", "Bounty", "Snickers"}
sweet_things = {"Muffins", "Snickers", "Candy Floss"}

#the difference method returns a new set 
#with elements that are unique to the set invoking the method
print(candy_bars.difference(sweet_things))
print(candy_bars - sweet_things)

print(sweet_things.difference(candy_bars))
print(sweet_things - candy_bars)