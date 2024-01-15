import random



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
lessThan = int(input("Please enter the number you would like to use to check against the list."))
k = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
j = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

paliString = str(input("Please enter a string to see if it is a palindrome!"))



for i in range(len(a)):
    if a[i] < lessThan:
        b.append(a[i])
print(b)

def loDivisors(numb):
    loD = []
    for i in range(1, numb):
        if numb % i == 0:
            loD.append(i)
            
    print(loD)

def elementsInCommon(loi1, loi2):
    commonElements = list(set(loi1) & set(loi2))
    return commonElements
    

def paliChecker(input_string):
    input_string = ''.join(input_string.split()).lower()
    if input_string == input_string[::-1]:
        print("This is a palindrome!")
    else:
        print("Not a palindrome")
    
    
    



paliChecker(paliString)
loDivisors(lessThan)
print(elementsInCommon(j,k))
