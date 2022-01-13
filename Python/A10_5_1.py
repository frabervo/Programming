text=open("C:\\Users\\E1376231\\Desktop\\Document.txt").readlines()
fobj=open("C:\\Users\\E1376231\\Desktop\\Document2.txt","w")
iterator=0
length= len(text)
for index in range(length):
    lineout=text[iterator].rstrip() + " " + text[iterator+1].rstrip() + "\n"
    fobj.write(lineout)
    iterator +=2
    if iterator==length:
        break     
#print(fobj)

fobj.close()