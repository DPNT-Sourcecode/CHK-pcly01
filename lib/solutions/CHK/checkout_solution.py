prices = { 'A': 50,'B': 30,'C': 20,'D': 15 }

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not skus:
        raise ValueError('no input provided')

    res = {}

    for s in skus.replace(' ','').upper():
        res[s] = res.get(s, 0) + 1

    total = 0

    for r in res.keys():
        if not r in prices:
            raise ValueError('invalid sku')
        total += (res[r] * prices[r])

    return total