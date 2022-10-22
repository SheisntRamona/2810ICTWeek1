#task2
# x = 2000
# while x >= 2000:
#     x += 1
#     if (x % 7 == 0) & (x % 5 != 0):
#         print(x)
#     if x == 2100:
#         break

#task3:1
def timeToSec(x):

    hours = int(x[:2])*3600
    minutes = int(x[2:5])*60
    seconds = int(x[-2:])

    output = hours+minutes+seconds

    print("Output:", output)
    return output

#timeToSec(input("input a time interval as H MM SS: "))

#task 3:2
def changeGive(x):

    Fcoin = int(int(x)/50)
    left = int(x) - Fcoin * 50

    Tcoin = int(int(left)/20)
    left = int(x) - (Fcoin*50 + Tcoin*20)

    tcoin = int(int(left)/10)
    left = int(x) - (Fcoin*50 + Tcoin*20 + tcoin*10)

    fcoin = int(int(left)/5)
    left = int(x) - (Fcoin * 50 + Tcoin * 20 + tcoin * 10 + fcoin * 5)

    ocoin = left

    print(Fcoin, Tcoin, tcoin, fcoin, ocoin)


# changeGive(int(input("Cost of item: ")))

#task3:3
def greaterZero(x):


    if x > 0:
        answer = True
    else:
        answer = False

    print(answer)

# greaterZero(int(input("enter an integer: ")))

#task 3:4
def twoInts(x):

    a, b = x.split()
    a = int(a)
    b = int(b)

    answer = bool((a in range(100) and a < b) or (a > 2*b and (b not in range(-8, 16) or b == 0)))
    print("Output: ", answer)

#twoInts(input("Input: "))

#task 3:5
def evenSpace(x):

    a, b, c = x.split(" ")

    a = int(a)
    b = int(b)
    c = int(c)

    answer = False

    # a > b > c
    if (a > b) and (b > c):
        if (a - b) == (b - c):
            answer = True
    # a > c > b
    elif (a > c) and (c > b):
        if (a - c) == (c - b):
            answer = True
    # b > c > a
    elif (b > c) and (c > a):
        if (b - c) == (c - a):
            answer = True
    # b > a > c
    elif (b > a) and (a > c):
        if (b - a) == (a - c):
            answer = True
    # c > b > a
    elif (c > b) and (b > a):
        if (c - b) == (b - a):
            answer = True
    # c > a > b
    elif (c > a) and (a > b):
        if (c - a) == (a - b):
            answer = True
    else:
        answer = False

    print(answer)

#evenSpace(input("input 3 ints: "))

#task 3:6
def sumOf(x):

    total = 0

    for n in range(0, int(x)+1):
        total += int(n)

    print("Output:", total)


#sumOf(input("Input: "))

#task 3:7
def twostrings(x):

    a, b = x.split(",")

    if len(a) == 0 & len(b) == 0:
        newstring = "@@"
    elif len(a) == 0:
        newstring = "@"+b[-1]
    elif len(b) == 0:
        newstring = a[0] + "@"
    else:
        newstring = a[0]+b[-1]

    print("Output: ", newstring)

#twostrings(input("Input: "))

#task 3:8
def concatstrings(x):

    x = x.strip()
    a, b = x.split(",")

    if len(a) == 0:
        concatstr = b
    elif len(b) == 0:
        concatstr = a
    elif a[-1] == b[0]:
        concatstr = a[0:-1]+b
    else:
        concatstr = a + b

    print("Output: ", concatstr.strip(" "))

#concatstrings(input("Input: "))

#task 3:9
def addsumto(x):

    count = 0
    total = 0
    totaltwo = 0

    while x > count:
        count += 1
        total += count

    for i in range(0, int(x)+1):
        totaltwo += i

    print("Output: ", total, totaltwo)

#addsumto(int(input("Input: ")))

#task 3:10
def stringMaker(x):

    a, b = x.split(",")

    if len(a) > len(b):
        string = b.strip()+a.strip()+b.strip()

    else:
        string = a.strip()+b.strip()+a.strip()

    print("Output: ", string)

#stringMaker(input("Input: "))

#task3:11
def missingChars(x):

    x.strip()

    if x[0] == "a" and x[1] == "b":
        string = x
    elif x[0] == "a":
        string = x[0]+x[2:]
    elif x[1] == "b":
        string = x[1:]
    else:
        string = x[2:]

    print("Output: ", string)

#missingChars(input("Input: "))

#task3:12
def listInts(x):

    listt = x.split()

    if '6' in listt:
        answer = True

    else:
        answer = False

    print("Output: ", answer)

#listInts(input("Input: "))

#task 3:13
def countClumps(x):

    clumps = 0
    arr = x.split(" ")
    i = 0

    while (i < len(arr) - 1):
        flag = 0
        while (i + 1 < len(arr) and
               arr[i] == arr[i + 1]):
            flag = 1
            i += 1
        if (flag):
            clumps += 1
        i += 1

    print("output: ", clumps)

#countClumps(input("Input: "))

#task 3:14
def filereader(f):

    file = open(f, "rt")
    filer = file.read()
    splitlist = filer.split()
    count = 0

    for word in splitlist:
        count += 1

    print("Output: ", count)

#filereader(input("File name: "))

#task3:15
def modelist(x):

    lst = x.split()
    newlst = []
    i = 0

    while i in range(len(lst)):
        newlst.append(int(lst[i]))
        i += 1

    newlst.sort()
    diff = int(newlst[-1]) - int(newlst[0])

    print(diff)

#modelist(input("Input: "))

#task 3:16
class Business:

    def __init__(self, name, address, fyear, email, phone):
        self.name = name
        self.address = address
        self.fyear = fyear
        self.email = email
        self.phone = phone

    def changePhone(self, newphone):
        self.phone = newphone
