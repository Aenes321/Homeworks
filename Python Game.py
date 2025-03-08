import numpy as np
import random
T='T'
M='M'
P='P'
S='S'
V='V'
E='E'
b=' '
point=0
sword=0
potion=0
saha=np.array([T,T,T,T,T,M,M,M,M,M,S,S,P,P,P,V,V,V,E,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b,b])
random.shuffle(saha)
sahashow=saha
for i in range(42):
    if sahashow[i]== 'T'or sahashow[i]=='M'or sahashow[i]=='S'or sahashow[i]=='P'or sahashow[i]=='V':
        sahashow=np.delete(sahashow,i)
        sahashow=np.insert(sahashow,i,' ')
newsahashow=sahashow.reshape(6,7)
newsaha=saha.reshape(6,7)
#print(newsaha) open for see backround
print("                       ")
print(newsahashow)
where=np.where(saha=='E') 
konum=where[0][0]
m=True
def arti1():
    global point
    point+=1
    print("--------------")
    print("+TREASURE")
def sword_arti():
    global sword
    sword+=1
    print("-----------------")
    print("+SWORD")
def potion_arti():
    global potion
    potion+=1
    print("-------------------")
    print("+POTİON")
def monster():
    global sword
    global potion
    global m
    print("Oh no monster!!!")
    if sword==0:
        print("YOU DİE.")
        print("The game ends")
        m=False
    else:
        sword-=1
        print("Sword is used")
def venom():
    global sword
    global potion
    global m
    print("Oh no Venom!!!" )
    if potion==0:
        print("You die.")
        print("The game ends")
        m=False
    else:
        potion-=1
        print("Potion is used")
def showing(x,y):
    global sahashow
    if y=='T':
        sahashow=np.delete(sahashow,x)
        sahashow=np.insert(sahashow,x,'E')
    elif y=='V':
        sahashow=np.delete(sahashow,x)
        sahashow=np.insert(sahashow,x,'E')
    elif y=='M':
        sahashow=np.delete(sahashow,x)
        sahashow=np.insert(sahashow,x,'E')
    elif y=='S':
        sahashow=np.delete(sahashow,x)
        sahashow=np.insert(sahashow,x,'E')
    elif y=='P':
        sahashow=np.delete(sahashow,x)
        sahashow=np.insert(sahashow,x,'E')
def up():
    global saha
    global sahashow
    global konum
    global newsaha
    global newsahashow
    if saha[konum-7]=='T':
        arti1()
        showing(konum-7,'T')
    elif saha[konum-7]=='V':
        venom()
        showing(konum-7,'V')
    elif saha[konum-7]=='M':
        monster()
        showing(konum-7,'M')
    elif saha[konum-7]=='P':
        potion_arti()
        showing(konum-7,'P')
    elif saha[konum-7]=='S':
        sword_arti()
        showing(konum-7,'S')
    elif saha[konum-7]=='E':
        print("You have already visited here!!!")
        konum+=7
    else:
        saha=np.delete(saha,konum-7)
        saha=np.insert(saha,konum-7,'E')
        sahashow=np.delete(sahashow,konum-7)
        sahashow=np.insert(sahashow,konum-7,'E')
    konum-=7
    newsaha=saha.reshape(6,7)
    newsahashow=sahashow.reshape(6,7)
    
def down():
    global saha
    global sahashow
    global konum
    global newsaha
    global newsahashow
    if saha[konum+7]=='T':
        arti1()
        showing(konum+7,'T')
    elif saha[konum+7]=='V':
        venom()
        showing(konum+7,'V')
    elif saha[konum+7]=='M':
        monster()
        showing(konum+7,'M')
    elif saha[konum+7]=='P':
        potion_arti()
        showing(konum+7,'P')
    elif saha[konum+7]=='S':
        sword_arti()
        showing(konum+7,'S')
    elif saha[konum+7]=='E':
        print("You have already visited here!!!")
        konum-=7
    else:
        saha=np.delete(saha,konum+7)
        saha=np.insert(saha,konum+7,'E')
        sahashow=np.delete(sahashow,konum+7)
        sahashow=np.insert(sahashow,konum+7,'E')
    konum+=7
    newsaha=saha.reshape(6,7)
    newsahashow=sahashow.reshape(6,7)
    
def left():
    global saha
    global sahashow
    global konum
    global newsaha
    global newsahashow
    if saha[konum-1]=='T':
        arti1()
        showing(konum-1,'T')
    elif saha[konum-1]=='V':
        venom()
        showing(konum-1,'V')
    elif saha[konum-1]=='M':
        monster()
        showing(konum-1,'M')
    elif saha[konum-1]=='P':
        potion_arti()
        showing(konum-1,'P')
    elif saha[konum-1]=='S':
        sword_arti()
        showing(konum-1,'S')
    elif saha[konum-1]=='E':
        print("You have already visited here!!!")
        konum+=1
    else:
        saha=np.delete(saha,konum-1)
        saha=np.insert(saha,konum-1,'E')
        sahashow=np.delete(sahashow,konum-1)
        sahashow=np.insert(sahashow,konum-1,'E')
    konum-=1
    newsaha=saha.reshape(6,7)
    newsahashow=sahashow.reshape(6,7)
    
def right():
    global saha
    global sahashow
    global konum
    global newsaha
    global newsahashow
    if saha[konum+1]=='T':
        arti1()
        showing(konum+1,'T')
    elif saha[konum+1]=='V':
        venom()
        showing(konum+1,'V')
    elif saha[konum+1]=='M':
        monster()
        showing(konum+1,'M')
    elif saha[konum+1]=='P':
        potion_arti()
        showing(konum+1,'P')
    elif saha[konum+1]=='S':
        sword_arti()
        showing(konum+1,'S')
    elif saha[konum+1]=='E':
        print("You have already visited here!!!")
        konum-=1
    else:
        saha=np.delete(saha,konum+1)
        saha=np.insert(saha,konum+1,'E')
        sahashow=np.delete(sahashow,konum+1)
        sahashow=np.insert(sahashow,konum+1,'E')
    konum+=1
    newsaha=saha.reshape(6,7)
    newsahashow=sahashow.reshape(6,7)
    

while m==True:
    a=input("Press L,R,U,D to move ")
    print("\033[H\033[J", end="")
    if a=="l" or a=="L":
       left()
    elif a=="r" or a=="R":
       right()
    elif a=="u" or a=="U":
        up()
    elif a=="d" or a=="D":
        down()
    #print(newsaha) open for see backgraound
    print("---------------------------------")
    print(newsahashow)
    print("Score:",point,"Sword:",sword,"Poition:",potion)
    
