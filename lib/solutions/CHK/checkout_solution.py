prices = { 'A': 50,'B': 30,'C': 20,'D': 15,'E': 40,'F': 10,'G': 20,'H': 10,'I': 35,'J': 60,'K': 70,'L': 90,'M': 15,'N': 40,'O': 10,'P': 50,'Q': 30,'R': 50,'S': 20,'T': 20,'U': 40,'V': 50,'W': 20,'X': 17,'Y': 20,'Z': 21 }
new_offers = [
    {'counts': {'A': 5}, 'price': 200},
    {'counts': {'A': 3}, 'price': 130},
    {'counts': {'E': 2, 'B': 1}, 'price': 80},
    {'counts': {'B': 2}, 'price': 45},
    {'counts': {'F': 3}, 'price': 20},
    {'counts': {'H': 10}, 'price': 80},
    {'counts': {'H': 5}, 'price': 45},
    {'counts': {'K': 2}, 'price': 120},
    {'counts': {'N': 3, 'M': 1}, 'price': 120},
    {'counts': {'P': 5}, 'price': 200},
    {'counts': {'R': 3, 'Q': 1}, 'price': 150},
    {'counts': {'Q': 3}, 'price': 80},
    {'counts': {'U': 4}, 'price': 120},
    {'counts': {'V': 3}, 'price': 130},
    {'counts': {'V': 2}, 'price': 90},
    {'counts': {'ZSTYX': 3}, 'price': 45}, # order important to remove most expensive first
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
        times_met = offer_met(res, offer['counts'])
        if times_met > 0:
            total += (offer['price'] * times_met)
            for o in offer['counts']:
                res[o] = res.get(o, 0) - (offer['counts'][o] * times_met)


    for r in res.keys():
        if not r in prices:
            return -1
        total += (res[r] * prices[r])

    return total

def offer_met(results, offer_count):
    times_matched = 1000
    for o in offer_count:
        if 
        if o in results:
            if results[o] < offer_count[o]:
                return 0
            else:
                matched_count = results[o] // offer_count[o]
                if matched_count < times_matched:
                    times_matched = matched_count
        else:
            return 0
    if times_matched == 1000:
        return 0
    return times_matched
