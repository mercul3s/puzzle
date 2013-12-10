
# This is the Cards Against Humanity Holiday Bullshit puzzle.
# I'm attempting to solve it with code.

frequency = {}
alphabet  = map(chr, range(65, 91))
code      = "GR QRW WKURZ DZDB DBQWKLQJ ZH VHQG BRX"

# first, we'll iterate through the string and count the
# frequency of the letters' occurrence.

for letter in code:
    if letter == " ":
        continue
    elif letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print frequency