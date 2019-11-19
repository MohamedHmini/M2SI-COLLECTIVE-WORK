
def maximum(l):
    return sorted(l)[-1]

def maximum2(l):
    return max(l)

def maximum3(l):
    m=0
    for i in l:
        if i>m:
            m=i
    return m

if __name__ == "__main__":
    l = [1,2,2,3,18,5]
    print(maximum(l))
    print(maximum2(l))
    print(maximum3(l))