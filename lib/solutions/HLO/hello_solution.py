

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not friend_name:
        raise ValueError('no input provided')
    return f'Hello, {friend_name.capitalize()}!'

