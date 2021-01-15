def solution(citations):
    citations.sort()
    min = 0
    mid = int(len(citations) / 2)
    max = len(citations)-1
    print(mid)

    while min < max :
        temp = mid
        mid = int((min+max) / 2)
        
        if citations[mid] >= mid+1 :
            min = mid+1
        elif citations[mid] <= mid+1 :
            max = mid-1
        else :
            break

    answer = temp
    print(answer)
    return answer


solution([0, 1, 1, 1, 3, 5, 7])