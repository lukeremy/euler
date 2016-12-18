# create ABC.. total score for each name
# A= 1, B = 2, C = 3, etc.
# multiply name score by ABC order position in list
# find sum of all scores

import pandas as pd

values = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

names = pd.read_csv('names.txt',header=None,delimiter=',')
names = names.transpose()
print names.head()

names.sort_values(by=0,inplace=True)
names.dropna(inplace=True)
names = names.reset_index(drop=True)
print names.head()
print names.tail()

print "first name:"
print names[0][0]
print "name #938:"
print names[0][937]

names = names[0]

all_sum = 0
for name in names:
    letter_score = 0

    print name
    letter_list = list(name)
    print letter_list
    while len(letter_list) > 0:
        letter_score += values[letter_list[0]]
        letter_list = letter_list[1:]
    # print "total letter score for {}: ".format(name) +str(letter_score)
    
    position =  list(names).index(name) + 1
    name_score = position*letter_score
    print "total score for {}: ".format(name) +str(name_score)
    all_sum += name_score
    print "sum after {}: ".format(name)+str(all_sum)
    

print "sum of all name scores: "+str(all_sum)
