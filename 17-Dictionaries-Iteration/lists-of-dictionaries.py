concert_attendees = [
    {"name": " Taylor", "row": 300, "price": 78.99},
    {"name": " Derek", "row": 200, "price": 98.99},
    {"name": " Ada", "row": 100, "price": 178.99}
]

for people in concert_attendees:
    for key, values in people.items():
        print(f"The {key} is {values}")