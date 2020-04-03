p = {12: 13, 1: 34, 15: 4}
print((sorted(p.items(), key=lambda x: x[1], reverse=True)))
