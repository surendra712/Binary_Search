def BinarySearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
l=[]
n=int(input("Enter no.of elements:"))
print("Enter elements:")
for i in range(n):
    e=int(input())
    l.append(e)
l.sort()
key=int(input("Enter the element to be found:"))
low=0

