# Python Challenge
# Solution to challenge 2

# Hint: "find rare characters in the mess below"

# Assumptions:
#   - Rare characters will be be alphabetic, lower case
#   - No alphabetic, lower case characters are not rare

f = open("Data_2")
s = f.read()

result = ""

for letter in s:
    if letter <= 'z' and letter >= 'a':
        result += letter

print (result)

# Result:
#   equality
