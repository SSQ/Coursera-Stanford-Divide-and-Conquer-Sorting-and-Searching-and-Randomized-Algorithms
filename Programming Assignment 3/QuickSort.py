#It's written in python3

with open('c:/Users/Nabin/Desktop/output.txt') as f:
    a = [int(x) for x in f]

    
#It's for the 3rd part of the assignment where we are told to use the median of three
def FindMedian(A): 
    minvalue = min(A)
    maxvalue = max(A)
    for i in range(3):
        if A[i] != minvalue and A[i] != maxvalue:
            return A[i]


#It's a function which chooses the pivot either the first elem for flag1, the last for flag2 and the median of three for flag3
def ChoosePivot(A,flag):
    n = len(A)
    first = A[0]
    final = A[n-1]
    if(n%2==0):
        k = n//2 - 1
        middle = A[k]
    elif(n%2!=0):
        k = n//2
        middle = A[k]
    else:
        print('error in ChoosePivot to choose middle element of A')

    B = [first,middle,final]
    med = FindMedian(B)
    if med==B[0]:
        position = 0
    elif med==B[1]:
        position = k
    else:
        position = n-1
        
    if flag==1:
        return 0
    if flag==2:
        return n-1
    if flag==3:
        return position
    else:
        print('wrong flag')

#Just a normal swap function
def Swap(A,first,second):
    second_value = A[second]
    first_value = A[first]
    A[first] = second_value
    A[second] = first_value
    return A

#It's where the main work is done.Comparing the elements. Here we always use the first element as a pivot than continue our comparison and swap.It places the the pivot value in it's proper position in the list
def Partition(A):
    pivot = A[0]
    r = len(A)
    i = 1
    for j in range(1,r):
        if A[j]<pivot:
            A = Swap(A,i,j)
            i +=1
    A = Swap(A,0,i-1)
    return A,i-1


#The main function where recursion is called
def QuickSort(A,flag):
    n = len(A)
    
    if n>1:
        p = ChoosePivot(A,flag)
        A = Swap(A,0,p) #places the pivot element in the first position as our partition function works assuming the first element is the pivot.
        A,pivot_position = Partition(A)
        A[:pivot_position],left = QuickSort(A[:pivot_position],flag)
        A[pivot_position+1:],right = QuickSort(A[pivot_position+1:],flag)
        
        return A,left+right+n-1 #for each recursive call atleast n-1 comparison is made and then it works for the left and right sublist.
    else:
        return A,0
