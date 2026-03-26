'''
def totalValue(lists):
    total = 0

    for row in lists:        
        for num in row:     
            total += num    
    return total


print(totalValue([[1,2],[3,4,5]]))
print(totalValue([[99,2,3],[3,4,5],[3,3]]))
print(totalValue([[1,2,3],[3,4,5],[3,3]]))
print(totalValue([[1]]))
print(totalValue([[2],[3]]))
print(totalValue([[1],[2],[3],[4],[5]]))
print(totalValue([[1,2],[3,-4,5],[5,6,-7,8,9,0]]))
print(totalValue([[7,2]]))
print(totalValue([[2,2,2,2,2],[3,5,6,7,8,9]]))
print(totalValue([[1],[2,0,-55],[3],[4,3,4],[5,3]]))

'''
def sumGreaterValues(lists):

    firstNum = lists[0][0]
    total = 0
    found = False

    for row in lists:
        for num in row:
            if num > firstNum:
                total += num
                found = True

    if found:
        return total
    else:
        return -1


print(sumGreaterValues([[1,2],[3,4,5]]))
print(sumGreaterValues([[99,2,3],[3,4,5],[3,3]]))
print(sumGreaterValues([[1,2,3],[3,4,5],[3,3]]))
print(sumGreaterValues([[1]]))
print(sumGreaterValues([[2],[3]]))
print(sumGreaterValues([[1],[2],[3],[4],[5]]))
print(sumGreaterValues([[1,2],[3,-4,5],[5,6,-7,8,9,0]]))
print(sumGreaterValues([[7,2]]))
print(sumGreaterValues ([[2,2,2,2,2],[3,5,6,7,8,9]]))
print(sumGreaterValues([[1],[2,0,-55],[3],[4,3,4],[5,3]]))
