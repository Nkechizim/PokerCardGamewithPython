units = ["meters", "kilograms", "litres", "ampere", "kelvin", "mole"]
print(len(units))

second_units = units.copy()

print(units)
print(second_units)

units.remove("kelvin")
print(units)
print(second_units)

new_units = units[:]
print(new_units)