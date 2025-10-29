import random
from helper import *

init()

while True:
    x = random.randint(0,120)
    print(x)
    

    
    
    # 0 - 15 ==> Punainen
    if x >= 0 and x <= 15:
        color = "red"
    # 95-100 ==> Sininen
    elif x >= 95 and x <= 100:
        color = "blue"
    # 35-55  ==> jos parilline: keltainen, jos pariton: vihreä
    elif x >= 35 and x <= 55:
        color = "green"
    # MUUT ROSKIIN (else)
    else:
        color = "roska"

    animate(x, color)
    
