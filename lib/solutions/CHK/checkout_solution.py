prices = { 'A': 50,'B': 30,'C': 20,'D': 15,'E': 40 }
offers = { 'A': {'count': 3, 'price': 130 },'B': {'count': 2, 'price': 45 }}
new_offers = [
    {'counts': {'A': 5}, 'price': 200},
    {'counts': {'A': 3}, 'price': 130},
    {'counts': {'E': 2, 'B': 1}, 'price': 80},
    {'counts': {'B': 2}, 'price': 45},
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not skus:
        return 0

    res = {}

    for s in skus.replace(' ',''):
        res[s] = res.get(s, 0) + 1

    total = 0

    for offer in new_offers:
        if offer_met(res, offer['counts']):
            total += offer['price']
            for o in offer['counts']:
                res[o] = res.get(o, 0) - offer['counts'][o]

    for r in res.keys():
        if not r in prices:
            return -1
        # if r in offers:
        #     num_of_offer = res[r] // offers[r]['count']
        #     if num_of_offer > 0:
        #         total += offers[r]['price'] * num_of_offer
        #         res[r] = res[r] % offers[r]['count']
        total += (res[r] * prices[r])

    return total

def offer_met(results, offer_count):
    for o in offer_count:
        if o results and results[o] < offer_count[o]:
            return False
    return True



