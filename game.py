import random

n=0
f=-1
l=['2','4','8','6']

class player:
    name=""
    power=100
    x=0
    y=0
    def __init__(self,name,x,y):
        self.name=name
        self.power=100
        self.x=x
        self.y=y

class enemy:
    ename=['enemy1','enemy2','enemy3']
    epower=['100','100','100']
    list_x=[]
    list_y=[]
    def __init__(self):
        self.ename=['enemy1','enemy2','enemy3']
        self.epower=[100,100,100]
        for x in range (0,3):
            self.list_x.append(random.randint(0, 5))
        for x in range (0, 3):
            self.list_y.append(random.randint(0, 5))

def fight(k):
	global n
	global f
	if f==1:
                print "you defeated",myenemy.ename[k],"." 
		myenemy.epower[k]=myenemy.epower[k]-you.power
	else:
                print "",myenemy.ename[k]," defeated you."
		you.power=you.power-myenemy.epower[k]
def move():
	global l
	global n
	global f
        mv=0
	if f==-1:
		mv=raw_input("Enter 8 to move up ward 6 to move right 4 to move left and 2 to move down : ")
		if mv=='8':
			if you.y+1<=5:
				you.y=you.y+1
				f=f*-1
			else:
				print "out of boundary try to move elsewhere"
		
		elif mv=='6':
			if you.x+1<=5:
				you.x=you.x+1
				f=f*-1
			else:
				print "out of boundary try to move elsewhere"
		elif mv=='4':
			if you.x-1>=0:
				you.x=you.x-1
				f=f*-1
			else:
				print "out of boundary try to move elsewhere"
		elif mv=='2':
			if you.y-1>=0:
				you.y=you.y-1
				f=f*-1
			else:
				print "out of boundary try to move elsewhere"
		
		else:
			print "Wrong option "
	else:
		mv=random.choice(l)
		if mv=='8':
			if myenemy.list_y[n]+1<=5:
				myenemy.list_y[n]=myenemy.list_y[n]+1
				f=f*-1
                                n=(n+1)%3
				
		elif mv=='6':
			if myenemy.list_x[n]+1<=5:
				myenemy.list_x[n]=myenemy.list_x[n]+1
				f=f*-1
			        n=(n+1)%3
		elif mv=='4':
			if myenemy.list_x[n]-1>=0:
				myenemy.list_x[n]=myenemy.list_x[n]-1
				f=f*-1
                                n=(n+1)%3
	
		elif mv=='2':
			if myenemy.list_y[n]-1>=0:
				myenemy.list_y[n]=myenemy.list_y[n]-1
				f=f*-1
                                n=(n+1)%3
print "Welcome to the game lets begin"
name=raw_input("Enter your name :")
x=raw_input("Enter x axis(0-5) :")
x=int(x)
y=raw_input("Enter y axis(0-5) :")
y=int(y)
you=player(name,x,y)
myenemy=enemy()
while ((myenemy.epower[0]>0 or myenemy.epower[1]>0 or myenemy.epower[2]>0) and (you.power>0)):
        print "You at (",you.x,",",you.y,") enemies at (",myenemy.list_x[0],",",myenemy.list_y[0],"),(",myenemy.list_x[1],",",myenemy.list_y[1],") and  (",myenemy.list_x[2],",",myenemy.list_y[2] ,")"
	if (you.x==myenemy.list_x[0] and you.y==myenemy.list_y[0]) and (myenemy.epower[0]>0):
		fight(0)
	elif (you.x==myenemy.list_x[1] and myenemy.list_y[1]==you.y) and (myenemy.epower[1]>0):
		fight(1)
	elif (you.x==myenemy.list_x[2] and myenemy.list_y[2]==you.y) and (myenemy.epower[2]>0):
		fight(2)
	else:	
		move()       
if (myenemy.epower[0]<=0 and myenemy.epower[1]<=0 and myenemy.epower[2]<=0):
	print "",you.name," won"
else:
        print "",you.name," lose"
