import random

choos=["palam","poloch"]
c_u=0
c_c1=0
c_c2=0

while True :
    user=input("enter your chooses:")
    computer1=random.choice(choos)
    computer2=random.choice(choos)
    print("Computer1:",computer1)
    print("Computer2:",computer2)

    if computer1=="palam":
        if computer2 =="palam":
            if user=="poloch":
                c_u+=1
    elif computer1=="poloch":
        if computer2 =="poloch":
            if user=="palam":
                c_u+=1
    elif user=="palam":
        if computer2 =="palam":
            if computer1=="poloch":
                c_c1+=1
    elif user=="poloch":
        if computer2 =="poloch":
            if computer1=="palam":
                c_c1+=1
    elif user=="palam":
        if computer1 =="palam":
            if computer2=="poloch":
                c_c2+=1
    elif user=="poloch":
        if computer1 =="poloch":
            if computer2=="palam":
                c_c2+=1
    if c_c1 == 5 or c_u == 5 or c_c2 ==5:
        break

if c_u== 5:
    print ("YOU WIN 🌼 ")  
elif c_c1== 5:
    print("YOU LOST computer1 win")
else:
     print("YOU LOST computer2 win")