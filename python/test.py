n = [3,5,7]
def double_list(x):
    print x
    res = []
    for i in range(0, len(n)):
        res.append(x[i] * 2)
#        res[i] = x[i] * 2
    return res

print double_list(n)

fu = []
fu[0] = 1
fu[1] = 2
print fu
