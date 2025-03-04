def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return (a*b)
def div(a,b):
    return (a/b) if b!=0 else "error"
print("Select the operation:\n1 = Addition\n2 = Subtraction\n3 = Multiplication\n4 = Division")
choice=int(input("enter the operation"))
n1=float(input("enter first number"))
n2=float(input("enter second number"))
if choice== 1:
    print(f"{n1}+{n2}=", add (n1,n2))
elif choice== 2:
    print(f"{n1}-{n2}=",sub (n1,n2)) 
elif choice== 3:
    print(f"{n1}*{n2}=",mul (n1,n2))
elif choice== 4:
        print(f"{n1}/{n2}=",div (n1,n2))
else:
    print("invalid") 
 