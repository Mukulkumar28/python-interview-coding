n =int(input("Enter a number"))
if n == 1:
    print("prime Number")
    if n>1:
        for i in range(2,n+1):
            if i%n ==0:
                print("Not a Prime Number")
            else:
                print("prime Number")
    