def shortestDistance(mylist, index):
    list_index = [index]
    list_finale = [mylist[index]]
    distFinale = 0
    for i in range(len(mylist) - 1):
        indexMin = - 1
        distMin = float('inf')

        for j in range(0, len(mylist)):
            dist = calculateDistance(mylist[list_index[-1]], mylist[j])
            if dist < distMin and list_index[-1] != j and j not in list_index:
                indexMin = j
                distMin = dist
        list_index.append(indexMin)
        list_finale.append(mylist[indexMin])
        distFinale = distFinale + distMin
    print(distFinale)
    print(list_index)
    return list_finale