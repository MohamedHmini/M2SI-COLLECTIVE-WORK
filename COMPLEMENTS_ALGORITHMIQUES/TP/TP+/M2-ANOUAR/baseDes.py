N = int(input())
nbd = int(input())
N_6 = N - nbd
i = 0
mx = 6**nbd
st = set()
while i < mx:
    k = i
    s = ''
    while k >= 0:
        s += str(k % 6)
        k //= 6
        if k == 0: 
            break

    x = sum( map(int, s) )
    if x == N_6:
        st.add( int(s) )
    i += 1

print(*st , sep = "\n", end='')


print(  )   