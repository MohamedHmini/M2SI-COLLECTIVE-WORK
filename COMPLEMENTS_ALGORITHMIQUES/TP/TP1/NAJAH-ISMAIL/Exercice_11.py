#Q1
def pui2(value=0):
    return int(value)**2

value = input("Saisir un nombre : ")
print("pui2("+value+") =",pui2(value))

#Q2
def pui4(value):
    return pui2(value)**2

print("pui4("+value+") =",pui4(value))