# Python Challenge
# Solution to challenge 3

# Hint: "One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."

f = open("Data_3")
s = f.read()

def isUpper(l):
    if l <= 'Z' and l >= 'A':
        return True
    return False

after = 0
before = 0
result = ""

for i in range(len(s)):
    if s[i] == '\n':
        continue
    elif not isUpper(s[i]):
        if after == 3 and before == 3:
            result += s[i - 4]
        before = after
        after = 0
    else:
        after += 1

print (result)

# Result:
#   linkedlist
