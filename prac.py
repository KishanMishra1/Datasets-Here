'''a,b,c=map(eval,input().split())
print(a,b,c)

a,b,c=b,c,a
print(a,b,c)

k=input()
s=""
for i in range(len(k)):
    s+=chr(ord(k[i])-32)
print(s)

k=input()
print(swapcase(k))

k=input()
k=k.upper()
print(k)


r=eval(input())
print(3.14*r*r)
print(3.14*2*r)


a=list(map(eval,input("Enter marks of students:\n").split()))
print(sum(a)/len(a))

a=eval(input("Enter the number:"))
print(1<<a);print(pow(a,3));print(pow(a,4));

from math import *

a,b,c=map(eval,input("Enter three sides of a triangle:").split())
s=(a+b+c)//2
#print(s)
res=sqrt(s*(s-a)*(s-b)*(s-c))
print(res)

p,r,t=map(eval,input("Enter principal amount,rate of interest and time period respectively:").split())
print((p*r*t)//100)


p,r,t,n=map(eval,input("Enter principal amount,rate of interest,time period and number of times compounded respectively:").split())
print(p*(1+(r/n))**(n*t))

x=eval(input("Enter a number:"))
print(x,2*x,3*x,4*x,5*x,sep="-")

    

s=input()
k=""
for i in s:
    k+=(chr(ord(i)-(1<<5)))
print(k)'''




    
