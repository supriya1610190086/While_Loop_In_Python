num=int(input("enter the number"))
n=num
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
if num%sum==0:
    print("harshad number")
else:
    print("not harshad number")