n=int(input("enter the lenth of the fibbnoic series"))
a=0
b=1
i=0
print("0")
print("1")
while i<=n:
    c=a+b
    a=b
    b=c
    i=i+1

   
    print(c)
