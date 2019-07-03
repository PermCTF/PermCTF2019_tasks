with open("D.txt","r") as file:
    flag = ''
    for line in file:
        line=line.strip()
        a,b,c = line.split(',')

        D = int(b)**2 - 4*int(a)*int(c)
        if D > 0:
            flag +=  '1'
        else:
            flag += '0'

    for i in range(0,round(len(flag)/7)):
        character = int(flag[7*i:7*(i+1)],2)
        print(chr(character),end='')
        # prikol s 7 bit kone4no
