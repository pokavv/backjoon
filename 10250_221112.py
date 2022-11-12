for i in range(int(input())):
    h, w, n = map(int, input().split())
    floor = 0
    ho = 0
    
    if n % h == 0:
        floor = h * 100
        ho = n // h
    else:
        floor = (n % h) * 100
        ho = 1 + n // h
    
    print(floor + ho)