score = [0,0,2,4,7,7,9]
score += [11,11,13,18]
score += [20]

stem_leaf = [[],[],[]]

for i in score :
    stem_leaf[int(i/10)].append(i%10)

print (stem_leaf)