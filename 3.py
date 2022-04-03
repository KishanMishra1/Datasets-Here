'''n=eval(input("Enter length (in cm):"))
if n>0:
    print(1/(2.54)*n)
else:
    print("Entry is invalid")

n=eval(input("Enter Temperature :"))
s=input("Unit of Temperature ?\n 'C' : Celsius \n 'F' : Fahrenheit\n Option :")
if s=="c" or s=="C":
    print((9/5)*n+32)
elif s=="f" or s=="F":
    print((5/9)*(n-32))
else:
    print("Invalid unit")

n=eval(input("Enter Temperature in Celsius:"))
if n<0:
    if n<-273.15:
        print("Temperature is invalid")
    elif n==-273.15:
        print("Temperature is absolute zero ")
    elif -273.15<n<0:
        print("Temperature is below freezing point")
elif n==0:
    print("Temperature is at freezing point")
elif 0<n<100:
    print("Temperature is in normal range")
elif n==100:
    print("Temperature at its boiling point")
elif n>100:
    print("Temperature above its boiling point")

n=eval(input("Enter the credits taken:"))
if n<=23:
    print("Student is a freshman")
elif 24<n<53:
    print("Student is a sophomore")
elif 54<n<83:
    print("Student is a junior")
else:
    print("Student is a senior")

n=int(input("How many items bought:"))
if n<10:
    print("Cost:",n*12)
elif 10<=n<=99:
    print("Cost:",n*10)
else:
    print("Cost:",n*7)


a,b=map(eval,input("Enter the two numbers:").split())
if abs(a-b)<=0.001:
    print("Close")
else:
    print("Not Close")

n=eval(input("Enter a year:"))
if n%4==0:
    if n%400==0 and n%100!=0:
        print("Its a Leap year")
    elif n%400!=0 and n%100!=0:
        print("Its a leap year")
    else:
        print("Its not a leap year")
else:
    print("Its not a leap year")

hr=eval(input("Enter a hour between 1 and 12:"))
ap=input("AM/PM:\n")
fhr=eval(input("How many years ahead ??"))
if fhr+hr>12:
    res=(fhr+hr)-12
    ap="PM"
else:
    res=fhr+hr
    ap+"AM"
print("{}{}".format((res),ap))'''

def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b, a%b)
    

    

    

