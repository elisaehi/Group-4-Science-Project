''''
# ---- GLOBAL VARIABLE ----
scores = [78, 85, 90, 66, 92]
def addBonus(lst, bonus):
    for i in range(len(lst)):
        lst[i] += bonus
#Add bonus marks to each score in the list. This function MUST modify the original list.

def dropLowest(lst):
    newScores = []
    newScores=lst[:]

    lowestScore = newScores[0]
    for i in newScores:
        if i < lowestScore:
            lowestScore = i
    
    newScores.remove(lowestScore)
    return newScores
# Return a NEW list with the lowest score removed. This function MUST NOT modify the original list.


curveScores = list(map(lambda x: x * 1.10))
def curveScores():
    global scores
    for i in range(len(scores)):
        scores[i] = int(scores[i]* 1.10)
    return scores
#Curve the GLOBAL 'scores' list by increasing all scores by 10%.This function MUST use the keyword 'global'.

def printReport(lst):
    avg = (sum(scores) // len(scores))
    print("the highest grade in your list is: ", max(scores))
    print("the lowest grade in your list is: ",min(scores))
    print("the average grade in your list is: ",avg)

# ---- MAIN EXECUTION ----
print("Original Scores:", scores)
addBonus(scores, 5)
print("After Bonus:", scores)
new_Scores = dropLowest(scores)
print("After Removing Lowest (new list):", new_Scores)
print("Scores should still be unchanged:", scores)
curveScores()
print("After Curving (global change):", scores)
printReport(scores)

'''
'''
a = 10
print(id(a))
b = a
a = a + 5

print("a=", a)
print("b=",b)
print("id(a)=", id(a))
print("id(b)=", id(b))
'''
'''
lst1 = [1,2,3]
lst2 = lst1
lst1[0] = 99

print("lst1 =", lst1)
print("lst2=",lst2)
print("id(lst1)=", id(lst1))
print("id(lst2)=", id(lst2))
'''
'''
squaredLambda = lambda x: x**2
print(squaredLambda(9))
'''
'''
power = lambda x, exp=2: x**exp
print(power(9))
'''

'''
numbers = [1,2,3]
squared = list(map(lambda x: x**2, numbers))
print(squared)

numbers = [1,2,3,4,5]
evenNumbers = list(filter(lambda x: x%2 == 0, numbers))
'''

points = [(2,3), (1,5), (4,1)]
sortedPoints = sorted(points, key=lambda x: x[1])
print(sortedPoints)
