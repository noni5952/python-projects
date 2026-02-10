word = input("शब्द दर्ज करें: ")

v = c = 0

for ch in word:
    if ch.lower() in "aeiou":
        v += 1
    else:
        c += 1

print("Vowels =", v)
print("Consonants =", c)
