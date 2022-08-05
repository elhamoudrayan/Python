import random as rd
from turtle import delay
from textwrap import wrap
listall=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', ',', '.', '<', '>']

num=input('Choose What You Want to do:\n1)Encrypt \n2)Decrypt \n0)Exit\nChoice: ')
if num=='1':
    try:
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
        name=input('What do you want to name your file: ')
        def main():
            outfile=open(f'{name}.txt','w')
            outfile.write(str(en_length) +'\n')
            outfile.write(encrypt +'\n')
            outfile.write(str(enclist))
            outfile.close()

        main()
    except:
        print('Something went wrong')
        quit()
if num=='2':
    try:
        path=input('Give me the path of the file you want to decrypt: ')
        decpass=''
        outfile=open(path,'r')
        wraping=int(outfile.readline())
        password = outfile.readline()
        declist = outfile.readline()
        outfile.close()


        declist=[declist[i:i+wraping] for i in range(0, len(declist), wraping)]
        password=[password[i:i+wraping] for i in range(0, len(password), wraping)]


        for letter in password:
            for element in declist:
                if letter==element:
                    lnume=declist.index(element)
                    decpass+=f'{listall[lnume]}'

        print(decpass)
    except:
        print('Something went wrong most likely in the encryption file make sure to restore it')
        quit()
else:
    quit()