import random

k= input('choose a diffculty level 1 for easy, 2 for medium, 3 for hard')

if k == '1':
    for i in range(10):
     p= random.randint(1,50)
     l= input('enter number')
     if l==p:
        print('you win')
        break
     else:
        print('you lose, the number was',p)

elif k == '2':
    for i in range(7):
     p= random.randint(1,100)
     l= input('enter number')
     if l==p:
        print('you win')
        break
     else:
        print('you lose, the number was',p)
else:
    
    for i in range(5):
        p= random.randint(1,500)
        l= input('enter number')
        if l==p:
             print('you win')
             break
        else:
             print('you lose, the number was',p)
