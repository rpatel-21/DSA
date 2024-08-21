def Pattern1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
        print("")

def Pattern2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("")
        
def Pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print("")

def Pattern4(n):
    for i in range(0,n):
        for j in range(1,n-i+1):
            print("*",end="")
        print("")
        

def Pattern5(n):
    for i in range(0,n):
        for j in range(1,n-i+1):
            print(j,end="")
        print("")
        
def Pattern4(n):
    for i in range(0,n):
        for j in range(1,n-i+1):
            print("*",end="")
        print("")
        
def Pattern6(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print("",end=" ")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,n-i-1):
            print("",end=" ")
        
        
        print("")
        
        
        
Pattern1(5)
print("")
Pattern2(5)
print("")
Pattern3(5)
print("")
Pattern4(5)
print("")
Pattern5(5)
print("")
Pattern6(5)