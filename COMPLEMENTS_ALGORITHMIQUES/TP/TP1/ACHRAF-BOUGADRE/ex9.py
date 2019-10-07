number_list = []
for i in range(1,4):
    number = int(raw_input('Enter number %d : ' % (i) ))
    number_list.append(number)
else :
    number_list.sort()

print number_list