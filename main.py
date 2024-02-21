# Functions in python Homework
def qudraticForumla1(a,b,c):
    root1 = (-b + (b**2 - 4*a*c)**0.5 /(2*a))
    return(root1)

def qudraticForumla2(a,b,c):
    root2= (-b - (b**2 - 4*a*c)**0.5 /(2*a))
    return(root2)


# TESTING IT
a = int(input("enter a value of a: "))
b = int(input("enter a value of b:"))
c = int(input("enter a value of c: "))

Result1 = qudraticForumla1(a,b,c)
Result2 = qudraticForumla2(a,b,c)

print(" The first root is", Result1)
print("The second root is", Result2)
quit()
