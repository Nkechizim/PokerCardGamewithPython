class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity

my_emotions = Emotion(98, 54)
other_emotions = Emotion(48, 74)

if my_emotions:
    print("You have a good emotional state")
else:
    print("You have a bad emotional state")

if other_emotions:
    print("You have a good emotional state")
else:
    print("You have a bad emotional state")

if [2, 5, 8]:
    print("hi")
else: 
    print("mo")