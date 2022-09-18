class Counter():
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        return two_counters

print(Counter.count)
c1 = Counter()
c2 = Counter()
print(Counter.count)

c3, c4 = Counter.create_two()
print(Counter.count)

print(c1.count)
print(c2.count)
print(c3.count)