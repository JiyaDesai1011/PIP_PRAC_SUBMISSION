Length = int(input())

MyList = []

i = 0
while i < Length:
    MyList.append(input())
    i += 1

print(" ")

def compare(j, k):
    List1 = list(j)
    List2 = list(k)
    List1.sort()
    List2.sort()

    if List1 == List2:
        print("YES")
    else:
        print("NO")


def slicer(s):
    if len(s) % 2 == 0:
        var = int(len(s)/2)
        List3 = []
        List3.append(s[:var])
        List3.append(s[var:])
        compare(List3[0], List3[1])
    else:
        var = int((len(s)+1)/2)
        List4 = []
        List4.append(s[:(var-1)]) 
        List4.append(s[var:]) 
        compare(List4[0], List4[1])


k = 0
while k < len(MyList):
    slicer(MyList[k])
    k += 1
