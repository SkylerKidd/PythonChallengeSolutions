# Python Challenge
# Solution to challenge 6

import zipfile as zf

z = zf.ZipFile('channel.zip')

def find_nothing(start_nothing):
    next_file = z.open(start_nothing + '.txt')
    file_data = next_file.read().decode('utf-8')
    comments = "" # Added post-result
    for i in range(1000):
        nothing = ""
        for char in file_data[len(file_data)-1:len(file_data)-6:-1]:
            if char >= '0' and char <= '9':
                nothing = char + nothing
        if nothing == "":
            break
        next_file = z.open(nothing + '.txt')
        file_info = z.getinfo(nothing + '.txt') # Added post-result
        print (nothing + '.txt')
        comments += str(file_info.comment.decode('utf-8')) # Added post-result
        file_data = next_file.read().decode('utf-8')
        print (file_data)
    print (comments) # Added post-result

# Starting 'nothing' from readme.txt
find_nothing('90052')

# Result:
#   Collect the comments.

# Post-result comments:
#   ***************************************************************
#   ****************************************************************
#   **                                                            **
#   **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
#   **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
#   **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
#   **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
#   **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
#   **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
#   **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
#   **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
#   **                                                            **
#   ****************************************************************
#    **************************************************************
