
# This is the Cards Against Humanity Holiday Bullshit puzzle.
# I'm attempting to solve it with code.

frequency = {}
alphabet  = map(chr, range(65, 91))
frequency_alphabet = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "L", "D", "C", "U", "M", "F", "P", "G", "W", "Y", "B", "V", "K", "X", "J", "Q", "Z"]
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