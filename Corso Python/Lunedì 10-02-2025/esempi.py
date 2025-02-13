def intero(val):
    if val.isdecimal():
        return int(val)
    else:
        return 0

listaN = ["uno","25","36","42","cinque","55"]
listaNI= []
for x in listaN:
    listaNI.append(intero(x))

listaNI2 = list(map(intero, listaN))
#print(listaNI2)

listaNI3 = [intero(x) for x in listaN]
#print(listaNI3)
#[0, 25, 36, 42, 0, 55]
def pariD(num):
    if num%2==0 and num !=0:
        return True
    else:
        return False

listaNu =[]
for ele in listaNI3:
    if pariD(ele):
        listaNu.append(ele)
#print(listaNu)

listaNu2 = list(filter(pariD,listaNI3))
print(listaNu2)

listaNu3 = [ele for ele in listaNI3 if pariD(ele)]

#print(listaNu3)