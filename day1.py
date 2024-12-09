
print( sum([ abs(o-p) for o,p in zip(*[sorted(y) for y in list(zip(*[( list(map(int, x.removesuffix("\n").split())) ) for x in open("inputs/1.txt").readlines()][::-1] ))]) ] ))