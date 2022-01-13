from typing import Iterator


max_iterator=int(input())
schritt=2
iterator=0
abstand=0.000000000000
ziel=2.500000000000
while iterator < max_iterator:
    abstand += 1 /(schritt**(iterator))
    iterator +=1
else:
    if(abstand>= ziel):
        print("Geschaft " + str(abstand))
    else:
        print("Nicht geschaft: "+ str(abstand))