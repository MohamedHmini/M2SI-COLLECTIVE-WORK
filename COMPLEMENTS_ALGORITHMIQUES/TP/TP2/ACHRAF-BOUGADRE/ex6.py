def fibo(n):
    u = [0, 1, None]
    print(0); 
    if n == 0 : 
        return
    print(1)
    if n == 1:
        return
    for i in map((lambda x: x%3), range(2, n)):
        u[i] = u[i-1] + u[i-2]
        print(u[i])


if __name__ == "__main__":
    n = int(input('n : '))
    fibo(n)