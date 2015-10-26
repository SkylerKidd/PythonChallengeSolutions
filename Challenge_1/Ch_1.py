# Python Challenge
# Solution to challenge 1

def tranStr(s):
    result = ""
    for letter in s:
        if letter < 'y' and letter >= 'a':
            result += chr(ord(letter) + 2)
        elif letter == 'y' or letter == 'z':
            result += chr(ord(letter) - 24)
        else:
            result += letter
    print (result)

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
tranStr(message)

# Result:
# i hope you didnt translate is by hand. thats what computers are for. doing it
# in by hand is inefficient and that's why this test is so long. using
# string.maketrans() is recommended. now apply on the url.

# So add the following:
urlMessage = "map"
tranStr(urlMessage)

# Result:
#   ocr
