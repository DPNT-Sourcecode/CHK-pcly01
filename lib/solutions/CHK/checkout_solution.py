prices = { 'A': 50,'B': 30,'C': 20,'D': 15 }
offers = { 'A': {'count': 3, 'price': 130 },'B': {'count': 2, 'price': 45 }}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not skus:
        return 0

    res = {}

    for s in skus.replace(' ',''):
        res[s] = res.get(s, 0) + 1

    total = 0

    for r in res.keys():
        if not r in prices:
            return -1
        if r in offers:
            num_of_offer = res[r] // offers[r]['count']
            if num_of_offer > 0:
                total += offers[r]['price'] * num_of_offer
                res[r] = res[r] % offers[r]['count']
        total += (res[r] * prices[r])

    return total
