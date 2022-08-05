import random as rd
from turtle import delay
from textwrap import wrap
listall=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', ',', '.', '<', '>']


print('TO START WE ARE GOING TO ASK YOU FOR A NUMBER WHICH WILL REPRESENT HOW MANY CHARACTER A LETTER WILL BE REPRESENTED AS; FOR EXEMPLE IF YOU GIVE ME *4* AS NUMBER THE LETTER *A* WILL BE REPRESENTED AS *DE4T*')
en_length=int(input("Give Me A Number: "))
newlist=[]
enclist=''
for i in range(0,81):
    rand=''
    for j in range(0,en_length):
        rand+=rd.choice(listall)
        while rand in newlist:
            rand=''
            rand+=rd.choice(listall)
    newlist.insert(i,rand)  
    enclist+=rand

print(newlist)

Pass=input('Give Me Your Password To Encrypt: ')

encrypt=''

for letter in Pass:
    for element in listall:
        if letter==element:
            lnume=listall.index(element)
            encrypt+=f'{newlist[lnume]}'

print(encrypt)

def main():
    outfile=open('data.txt','w')
    outfile.write(str(en_length) +'\n')
    outfile.write(encrypt +'\n')
    outfile.write(str(enclist))
    outfile.close()

main()


