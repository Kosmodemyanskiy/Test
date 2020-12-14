def CheckOnSimilarStrings():
    for i in range(len(a)):
        if(b.find(a[i]) == -1):
            return False
        elif a.count(a[i]) != b.count(a[i]):
            return False
    return True

a, b = input().lower().split(" ")

if len(a) != len(b):
    print("No")
else:
    if(CheckOnSimilarStrings()):
        print("Yes")
    else:
        print("No")
