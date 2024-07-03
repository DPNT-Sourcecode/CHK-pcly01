prices = { 'A': 50,'B': 30,'C': 20,'D': 15 }

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    res = {}

    for s in skus:
        res[s] = res.get(s, 0) + 1

    total = 0

    for r in res.keys():
        total = 
