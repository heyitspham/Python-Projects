import random
def getColor( ):
    lstColors = ['Red','Yellow','Blue','Green','Purple','Pink','White'   ,'Black']
    return lstColors        
color = random.choice(getColor())
print(color)
