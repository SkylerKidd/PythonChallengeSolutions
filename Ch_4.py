# Python Challenge
# Solution to challenge 4

import urllib.request as ur

def findNothing(current):
    urlBeg = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    response = ur.urlopen(urlBeg + current)
    data = response.read().decode('utf-8')
    for i in range(400):
        nothing = ""
        for char in data[len(data)-1:len(data)-6:-1]:
            if char >= '0' and char <= '9':
                nothing = char + nothing
        if nothing == "":
            break
        response = ur.urlopen(urlBeg + nothing)
        print (urlBeg + nothing)
        data = response.read().decode('utf-8')
        print (data)

findNothing('12345')

# Result:
#   Yes. Devide by two and keep going.
# Current 'nothing':
#   16044

findNothing('8022')

# Result:
#   peak.html
