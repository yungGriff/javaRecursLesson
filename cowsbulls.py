print("Welcome to the Cows and Bulls game!")
#user_input = list(input("Enter a 4 - digit number! "))
user_input = [1, 2, 4, 5]
test = [1, 2, 3, 4]
# test.split()
bull = 0 # every digit in the wrong place
cow = 0 # every digit in the correct place
iterator = 0
while iterator < 4:
    if test[iterator] == user_input[iterator]:
        cow += 1
    elif test[0] == user_input[iterator]:
        bull += 1
    elif test[1] == user_input[iterator]:
        bull += 1
    elif test[2] == user_input[iterator]:
        bull += 1
    elif test[3] == user_input[iterator]:
        bull += 1
    iterator += 1

print("You got yourself: " + str(cow) + " cow(s)")
print("You got yourself: " + str(bull) + " bull(s)")


def fibo(start, duration):
    seq = []
    if duration > 1:
        seq.append(start)
        seq.append(start)
        i = 0
        while(i + 1) < duration:
            nextInSequence = seq[i] + seq[i + 1]
            seq.append(nextInSequence)
            i += 1
    else:
        seq.append(start)
    print(seq)

def reverseAString(input_string):
    newStr = ""
    for char in input_string:
        newStr = char + newStr
    print(newStr)

def sliceStr(input_string):
    return input_string[::-1]

def removeDuplicates(loi1, loi2):
    return list(set(loi1) & set(loi2))
def removeDuplis(loi1, loi2):
    CL = []
    for i in loi1:
        if i not in loi2:
            CL.append(i)

def removeLowerCase(input_string):
    upperString = ""
    for char in input_string:
        if not char.islower():
            upperString += char
    return upperString
def removeUpperCases(input_string):
    lowerString = ""
    for char in input_string:
        if not char.isupper():
            lowerString += char
    return lowerString

def bubblesort(loi): #name the method that we are using to implement the bubble sort algorithm
    size = len(loi) #take the size of the input list
    swapped = False #create a flag to check whether or not a swap has taken place
    for i in range(size - 1): #for the duration of the length of the str paying attn to arr 0
        for j in range(0, size - i - 1): #making sure we dont roll over the list
            if loi[j] > loi[j + 1]: #if the first guy is larger than the guy after him
                swapped = True #flag that we are swapping /swapped
                loi[j], loi[j + 1] = loi[j + 1], loi[j] # 2,1 set to 1, 2
        if not swapped: #if the swap didnt take place
            return #return

    print(loi)

def bs(loi):
    list_size = len(loi)
    swapped = False
    for i in range(list_size - 1):
        for j in range(0, list_size - i - 1):
            if loi[j] > loi[j + 1]:
                swapped = True
                loi[j], loi[j + 1] = loi[j + 1], loi[j]
        if not swapped:
            return

    print(loi)


a = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8]
b = [2, 5, 7, 1, 2, 0, 8, 6, 5]
c = [2, 5, 7, 1, 2, 0, 8, 6, 5]

print(bs(b))
print(bubblesort(c))
hw = "Hello World"
#print(result)
print(removeUpperCases(hw))
print(removeLowerCase(hw))
#print(fibo(1, 10))
