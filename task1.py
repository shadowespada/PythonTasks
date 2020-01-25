# Programming task: Write a function that asks for first name and last  
# name as input and greets the person referring to that person’s full name.

def FullName (fname, lname):
    print(f"Good Morning {fname} {lname}")


fname = input("First Name: ")
lname = input("Last Name: ")
FullName(fname, lname)


