prices = { 'A': 50,'B': 30,'C': 20,'D': 15 }

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    res = {}

    for c in skus:
        res[c] = res.get(c, 0) + 1


