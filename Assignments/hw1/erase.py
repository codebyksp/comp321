import sys
N = int(input())
Line1 = input().strip()
Line2 = input().strip() 

if N % 2 != 0:
    str = ''
    for char in Line1:
        if char == "1":
            str += '0'
        else:
            str += '1'
    
    if str == Line2:
        print("Deletion succeeded") 
    else:
        print("Deletion failed")    
else:
    if Line1 == Line2:
        print("Deletion succeeded")         
    else:
        print("Deletion failed")