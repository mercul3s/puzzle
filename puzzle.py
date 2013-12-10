#!/usr/bin/python

from sys import argv

# This is the Cards Against Humanity Holiday Bullshit puzzle.
# I'm attempting to solve it with code.

code = argv[1]

frequency = {}
alphabet  = map(chr, range(65, 91))
frequency_alphabet = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "L", "D", "C", "U", "M", "F", "P", "G", "W", "Y", "B", "V", "K", "X", "J", "Q", "Z"]
new_code  = ""

# first, we'll iterate through the string and count the
# frequency of the letters' occurrence.
# we don't actually need this since I know what the cipher is now, but I'll keep it
# in case I need to analyze code later.
for letter in code:
    if letter == " ":
        continue
    elif letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

# Start substituting letters according to a Caesar Cipher (offset by 3 letters)
for letter in code:
    if letter == " ":
        new_code += letter
    elif ord(letter) > 67:
        ordinal = ord(letter) - 3
        new_code += chr(ordinal)
    else:
        ordinal = ord(letter) + 23
        # print chr(ordinal)
        new_code += chr(ordinal)

print "Cipher:     %s" % (code)
print "Deciphered: %s" % (new_code)