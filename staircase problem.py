n=int(input("enter the number of steps: "))
nways=0
if n%2==0:
    q=n//2
    for i in range(1,q+1):
        s=q+i
        nways+=s
    print("the stairs can be climbed in %d ways."%(nways))
else:
    nways=1
    q=n//2
    for i in range(1,q+1):
        s=q+i
        nways+=s
    print("the stairs can be climbed in %d ways."%(nways))
