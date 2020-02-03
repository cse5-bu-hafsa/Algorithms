'''
Hafsa Akter
Department of Computer Science & Engineering
5th Batch
Roll:18CSE012
University Of Barisal

'''
A=list(map(int,input("Enter Numbers:").split()))
#Source code of InsertionSort        
def InsertionSort(A):
    for j in range(1,len(A)):
        key=A[j];i=j-1
        while(i>-1 and A[i]>key):
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    print("After Insertion Sort: ",*A)
InsertionSort(A)
#end
#source code of Counting Sort
def countingSort(A):
    mx=max(A);ln=len(A)
    C=[0]*(mx+1)
    for i in A:
        C[i]=C[i]+1
    C[0]=C[0]-1
    for i in range(1,mx+1):
        C[i]=C[i]+C[i-1]
    B=[0]*len(A)
    for x in reversed(A):
        B[C[x]]=x
        C[x]=C[x]-1
    return B
print("After Counting Sort: ",*countingSort(A))
#end
#Source code of Selection Sort
def swap(a,b):
    tmp=a;a=b;b=tmp;

def selectionSort(A):
    C=[]
    for i in range(len(A)):
        mn=min(A[i:])
        swap(A[i],A[A.index(mn)])
    print("After Selection Sort: ",*A)
selectionSort(A)
#End
#Source code of Bubble Sort
        
def bubbleSort(A):
    for i in A:
        for j in range(i,len(A)):
            if (A[i]<=A[j]):
                swap(A[i],A[j])
    print("After Bubble Sort: ",*A)
bubbleSort(A)
#end
#Source code of merge sort
                
def mergeSort(A):
    if len(A) > 1:
        mid=len(A)//2;left=A[:mid];right = A[mid:];mergeSort(left);mergeSort(right);i=j=k=0;
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                A[k]=left[i];i+=1
            else:
                A[k]=right[j];j+=1
            k+=1
        # For all the remaining values
        while i<len(left):
            A[k]=left[i];i+=1;k+=1
        while j<len(right):
            A[k]=right[j];j+=1;k+=1

mergeSort(A)
print("After Merge Sort: ",*A)
#end
