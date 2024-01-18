import random
def watermelon(w):
    if 1 <= w <= 100:
        if w % 2 == 0:
            print("YES")
        else:
            print("Nope")
    else:
        print("Thanks not a watermelon dude, what")

def wordToLong(input_str):
    strSize = len(input_str)
    theMiddle = strSize - 2
    if strSize > 10:
        abv = str(input_str[0]) + str(theMiddle) + str(input_str[-1])
        return abv
    else:
        return input_str

def buildalist(x):
    listOfLists = []
    for i in range(x):
        li = []
        for i in range(3):
            li.append(random.randrange(0,2))
        listOfLists.append(li)

    return listOfLists

def listcomparitor(loi1, loi2):
    size1 = len(loi1)
    size2 = len(loi2)
    results = []
    if size1 > size2:
        for i in range(size1):
            if loi1[i] == loi2[i]:
                results.append(1)
            else:
                results.append(0)
    else:
        for i in range(size2):
            if loi1[i] == loi2[i]:
                results.append(1)
            else:
                results.append(0)
    return results
    def greeting(name):
  print("Hello there, " + name)


def romanToInteger(input_str):
  size = len(input_str)
  total = 0
  for i in range(size):
    if input_str[i] == "I":
      total += 1
    elif input_str[i] == "V":
      total += 5
    elif input_str[i] == "X":
      total += 10
    elif input_str[i] == "L":
      total += 50
    elif input_str[i] == "C":
      total += 100
    elif input_str[i] == "D":
      total += 500
    elif input_str[i] == "M":
      total += 1000
    else:
      return 0
  return total



testString = "localization"
result = wordToLong(testString)
print(result)
a = [0, 1, 1]
b = [1, 1, 1]
print(listcomparitor(a, b))

berry = 8
watermelon(berry)

