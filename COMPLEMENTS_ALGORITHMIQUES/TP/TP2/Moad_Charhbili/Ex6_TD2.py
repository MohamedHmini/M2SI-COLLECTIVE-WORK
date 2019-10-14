from Python_Algo.TP2.Moad_Charhbili.My_Functions import fibonacciNp1
def main():
    a = int(input('Saisir un entier : '))
    prev,cur=0,1
    for i in range(2,a+2):
        temp=prev
        prev=cur
        cur=cur+temp
        print(cur)
    print("fib",fibonacciNp1(a+1))
if __name__ == '__main__':
    main()