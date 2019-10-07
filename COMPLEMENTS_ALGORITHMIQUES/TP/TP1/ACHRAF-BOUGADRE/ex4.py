#not(not(a and b ) or False) = a and b

print "_"*23
print "a\t"   , "b\t" , "a and b"
print False ,"\t", False ,"\t",  False and False
print False ,"\t", True  ,"\t",  False and True
print True  ,"\t", False ,"\t",  True  and False
print True  ,"\t", True  ,"\t",  True  and True 
print "_"*23

#not(not(not(a) and b) and not(a and not(b)))
#==>(not(a) and b) or (a and not(b))
A = [False, True]
B = [False, True]

print "_"*48
print "a\t"   , "b\t" , "(not(a) and b) or (a and not(b))"
for a in A:
    for b in B:
        print a ,"\t", b ,"\t", (not(a) and b) or (a and not(b))

print "_"*48



print "_"*29
print "a\t"   , "b\t" , "(not(a) or b)"
for a in A:
    for b in B:
        print a ,"\t", b ,"\t", (not(a) or b)

print "_"*29