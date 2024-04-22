#program-1
if __name__ == '__main__':
    print("Hello, World!")

#program-2
if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n%2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
    print("Weird")
else:
    print("Not Weird")

#program-3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#program-4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#program-5
if __name__ == '__main__':
    n = int(input())
    sum = 0
    for i in range (0, n):
        print(i**2)

#program-6
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0 and year%100==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
    return leap
year = int(input())
print(is_leap(year))

#program-7 
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")

#program-8
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

#program-9
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))

#program-10
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a,b)+pow(c,d))