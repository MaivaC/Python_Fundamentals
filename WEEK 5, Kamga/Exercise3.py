#Find the maximum value

'''def find_max(a,b,c):

    if a>=b and a>=c:
     return a

    elif b>=a and b>=c:
      return b

    else:
       return c


x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))
 

print("Max number is:  ", find_max(x,y,z))'''


def find_max(a,b,c):
    return max(a,b,c)
print(find_max(10,6,7))
    