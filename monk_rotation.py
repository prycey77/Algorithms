testCase  = int(input())
for _ in range(testCase):
    n,k = map(int,input().split())
    
    l = list(map(int,input().split()))
    x = k%n
    print(x)
    print((*l[n-x:]+l[:n-x]))
