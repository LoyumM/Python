    # Size: 7 x 21 
    # ---------.|.---------
    # ------.|..|..|.------
    # ---.|..|..|..|..|.---
    # -------WELCOME-------7
    # ---.|..|..|..|..|.---
    # ------.|..|..|.------
    # ---------.|.--------- 
    
leng,brd = map(int,input().split())

if leng % 2 == 1:
    for rep in range(1,leng,2):
        print((rep*".|.").center(brd,"-"))
        
    print("WELCOME".center(brd,"-"))
        
    for rep in range(leng-2,0,-2):
        print((rep*".|.").center(brd,"-"))
else:
    print("Try an odd natural number")