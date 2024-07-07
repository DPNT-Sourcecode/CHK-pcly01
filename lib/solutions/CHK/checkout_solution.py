prices = { 'A': 50,'B': 30,'C': 20,'D': 15 }
offers = { 'A': {'count': 3, 'price': 130 },'B': {'count': 2, 'price': 45 }}

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
        if r in offers:
            
        total += (res[r] * prices[r])

    return total
