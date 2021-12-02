import random as r
import sys
def getNumber():
    in1=int(input("Enter a number between 1 to 6"))
    try:
        if(in1<1 or in1>6):
            raise Exception
    except:
        print("Choose between 1 to 6")
        sys.exit(j)
    return in1
def batting():
    score1=0
    while(True):
        x=getNumber()
        y=r.randint(1,6)
        
        if(x==y):
            print("Out!!!!!")
            print("Your Score is:",score1)
            return score1
            
        else:
            score1+=x
            print("Score:",score1)

def bowling():
    score2=0
    while(True):
        x=r.randint(1,6)
        y=getNumber()
        if(x==y):
            print("Out!!!")
            print("Your Score is:",score2)
            return score2
        else:
            score2+=x
            print("Score:",score2)
    
print("-"*190)
print("welcome to handcricket game")
print("the rules are simple\nRULES:::\n1.choose batting or bowling\n2.when you and cpu chooses the same number,the person who was batting will be considered as out\n3.the person whoo has higher score will be considered as winner\n4.the last ball before your out,wil also be included in your score")
choice=int(input("choose::\n1.batting\n2.bowling\n"))
if(choice==1):
    print("You picked Batting")
    s1=batting()
    print("Now you have to bowl.")
    print("Guess a number from 1 to 6")
    s2=bowling()
    if(s1>s2):
        print("You won")
    else:
        print("Computer won")
else:
    print("You picked bowling")
    print("Guess a number from 1 to 6")
    s1=bowling()
    print("Now you have to bat")
    s2=batting()
    if(s1>s2):
        print("You won")
    else:
        print("Computer won")