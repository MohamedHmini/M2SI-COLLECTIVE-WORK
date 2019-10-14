y = 1
def multEgyptienne(m, n):
    prod = 0
    while m > 0:
        if m % 2 == 0:
            m >>= 1
            n <<= 1
        elif m % 2 == 1:
            m -= 1
            prod += n 
    
    return prod
    

if __name__ == "__main__":
    print("15*387 = ",15*387)
    print("multEgyptienne(15, 387) = ", multEgyptienne(15, 387))