def ghostySubmarine(size, ghosts):
    ghosts.sort()
    totalArr = []
    combArr = []
    for num in ghosts:
        for everywhere in list(totalArr):
            totalArr.append(everywhere + num)
        totalArr.append(num)
        for combination in list(combArr):
            combArr.append(combination + [num])
        combArr.append([num])
    fat = -1
    record = 0
    for i in range(len(totalArr)):
        if totalArr[i] > fat and totalArr[i] < size:
            fat = totalArr[i]
            record = i
    if fat == -1:
        return []
    return combArr[record] 
    
subsize = 25
ghosts = [4,8,1,9,16,13,19]

print(ghostySubmarine(subsize, ghosts))