
def solution(absolutes, signs): return sum(absolutes[i] * (1 if signs[i] else -1) for i in range(len(signs)))

'''def solution(absolutes, signs):
    pl=sum(absolutes[x] for x in range(len(absolutes)) if signs[x])
    mi=sum(absolutes[x] for x in range(len(absolutes)) if not signs[x])
    return pl-mi'''