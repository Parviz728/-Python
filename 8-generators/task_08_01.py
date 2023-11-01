def myzip(*args):
    mx = len(max(args, key=len))
    for i in range(mx):
        for lst in args:
            if i < len(lst):
                yield lst[i]
                
            

ans = []
print(list(myzip(['A', 'B', 'C'], [1, 2, 3]))) # ['A', 1, 'B', 2, 'C', 3]
print(list(myzip('!', ['A', 'B', 'C', 'D'], range(1, 3)))) # ['!', 'A', 1, 'B', 2, 'C', 'D']
            