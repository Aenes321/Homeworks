class is_firmus:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def kural1(self):
        if 0 in self.x or 0 in self.y:
            a=True
        else :
            a=False
        if self.x[1]!=self.y[1]:
            if self.x[1]!=self.y[3]:
                if self.x[3]!=self.y[1]:
                    if self.x[3]!=self.y[3]:
                        b=False
                    else:
                        b=True
                else:
                    b=True
            else:
                b=True
        else :
            b=True
        x1=self.x[0]-self.x[2]
        if x1<0:
            x1*=-1
        x2=self.x[1]-self.x[3]
        if x2<0:
            x2*=-1
        y1=self.y[0]-self.y[2]
        if y1<0:
            y1*=-1
        y2=self.y[1]-self.y[3]
        if y2<0:
            y2*=-1
        alan1=x1*x2
        alan2=y1*y2
        toplamalan=alan1+alan2
        max1=max(self.x[1],self.x[3])
        max2=max(self.y[1],self.y[3])
        max3=max(max1,max2)
        max4=max(self.x[0],self.x[2])
        max5=max(self.y[0],self.y[2])
        max6=max(max4,max5)
        if max5-max4<0:
            maxfarkx=max4-max5
            print("1.sağda")
            if maxfarkx>x1:
                kesisim2=0
            elif maxfarkx==x1:
                kesisim2=3   #"bitişik"
            else:
                kesisim2=1
        else:
            maxfarkx=max5-max4
            print("2.sağda")
            if maxfarkx>y1:
                kesisim2=0
            elif maxfarkx==y1:
                kesisim2=3#bitişik
            else:
                kesisim2=1
        
        if max2-max1<0:
            maxfark=max1-max2
            print("1.yukarida")
            orta=self.x[0]+self.x[2]
            orta1=orta/2
            if self.y[0]<orta1<self.y[2]:
                kural3=True
            else :
                kural3=False
            if maxfark>x2:
                kesisim1=0
            elif maxfark==x2:
                kesisim1=3   #"bitişik"
            else:
                kesisim1=1
        else:
            maxfark=max2-max1
            print("2.yukarida")
            orta=self.y[0]+self.y[2]
            orta1=orta/2
            if self.x[0]<orta1<self.x[2]:
                kural3=True
            else:
                kural3=False
            if maxfark>y2:
                kesisim1=0
            elif maxfark==y2:
                kesisim1=3
            else:
                kesisim1=1
        if kesisim1+kesisim2==2:
            print("iki şekil kesisiyor fakat alani hesaplayamam gösterilen sonuçtan küçük olmali")
        if kesisim1!=3:
            b=False
        if a==True:
            if b==True:
                if kural3==True:
                    print("FİRMUS",toplamalan)
                else:
                    print("ADDENDUM","????")
            else:
                print("DAMNARE",toplamalan)

        else:
            print("DAMNARE",toplamalan)


figure1=is_firmus([0,0,2.4,5.2],[-8.7,10,0,0])
figure1.kural1()
