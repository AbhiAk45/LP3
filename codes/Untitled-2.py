def recursive(n):
    if n<=1:
        return n
    else:
        return recursive(n-1) + recursive(n-2)
    
n=int(input("enter no of terms"))
print("recursive")
for i in range(n):
    print(recursive(i),end='')


def non_recursive(n):
    a=0
    b=1
    for i in range(n):
        print(a,end='')
        c=a+b
        a=b
        b=c
print()
print("non recursive")
non_recursive(n)