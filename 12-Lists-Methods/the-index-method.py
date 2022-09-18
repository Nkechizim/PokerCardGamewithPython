def encrypt_message(string):
    letters = "abcdefghijklmnopqrstuvwxyzab"
    new = []
    for i in string:
        index = letters.index(i)
        new.append(letters[index + 2])
    return "".join(new)

print(encrypt_message("abc"))
print(encrypt_message("xyz"))

a = [4,5,6,7]
print(a)
print(list(range(a[0], a[-1]+1)))

rank_indexes = [4, 5, 6, 7]
last_index = rank_indexes[-1]
if rank_indexes == list(range(rank_indexes[0], rank_indexes[-1]+1)):
    #if len(self._card_suit_counts) > 1:
    print("Straight")