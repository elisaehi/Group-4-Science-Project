'''
def socialSecurity(number):
    if str(number)[3] == "-" and str(number)[6] == "-" and (len(number) == 11):
        return number[7:11]
    else:
        return "bad"
    
result = socialSecurity("222-49-1234")
print(result)
'''


def twoLetters(word):
    count = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    return count

result = twoLetters("")
print(result)


'''
def addUp(phrase):
    sum = 0
    for i in (phrase):
        if i in "123456789":
            sum += int(i)
    return(sum)
    print(sum)

result = addUp("hello5555")
print(result)
'''
