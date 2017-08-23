   
with open('IntegerArray.txt') as f:
    a = [int(x) for x in f]

def CountSplitInv(B,C):
    i = 0
    j = 0
    count = 0
    D = []
    while i<len(B) and j<len(C):
        D.extend([min(B[i],C[j])])
        if B[i] < C[j]:
            i = i + 1
        else:
            count +=len(B[i:])
            j+=1
    D.extend(B[i:])
    D.extend(C[j:])
    Z = count
    return D,Z

def Sort_Count(A):
    n = len(A)
    if n > 1:
        splitposition = n / 2
        B,X = Sort_Count(A[:-splitposition])
        C,Y = Sort_Count(A[-splitposition:])
        D,Z = CountSplitInv(B,C)
        return D,X+Y+Z
    else:
        return A,0

Sort_Count(a)
