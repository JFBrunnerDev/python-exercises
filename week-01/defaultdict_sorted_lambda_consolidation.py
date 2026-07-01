from collections import defaultdict

def filtering(method):
    d=defaultdict(list)
    for x in method:
        d[x[2]].append((x[0], x[1]))

    result={}
    for category, lists in d.items():
        f=defaultdict(int)
        for name, cost in lists:
            f[name] += cost
        result[category] = sorted(f.items(), key=lambda x: x[1], reverse=True)
        
    return result

if __name__=="__main__":
    transactions = [
        ("Alice", 120, "food"),
        ("Bob", 45, "tech"),
        ("Alice", 30, "tech"),
        ("Charlie", 200, "food"),
        ("Bob", 15, "food"),
        ("Alice", 90, "food"),
        ("Charlie", 60, "tech"),
    ]
    print(filtering(transactions))