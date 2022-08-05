from textwrap import wrap

listall=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', ',', '.', '<', '>']
decpass=''

outfile=open('data.txt','r')
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