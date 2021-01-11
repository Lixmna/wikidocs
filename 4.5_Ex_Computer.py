def pro2com(input,computer) :
    outlist = []
    sumout = []
    for i in range(computer) :
        outlist.append([])
        sumout.append(0)    

# for문 돌리면서 i가 사용되지 않았을때 warning 발생하는데 상관없는지

    input.sort(reverse=True)

    for time in input :
        lowComputer = sumout.index(min(sumout))
        outlist[lowComputer].append(time)
        sumout[lowComputer] += time

    return outlist


whitch_com = 0
for output in pro2com([3,15,7,22,13,2], 3) :
    whitch_com = whitch_com + 1
    print("computer"+str(whitch_com),":",output)
