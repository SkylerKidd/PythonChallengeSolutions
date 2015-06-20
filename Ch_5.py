# Python Challenge
# Solution to challenge 5

import pickle as pk

f = open("Data_5", "rb")
p = pk.load(f)

for each_dict in p:
    each_line = ""
    for each_pair in each_dict:
        for i in range(each_pair[1]):
            each_line += each_pair[0]
    print (each_line)
