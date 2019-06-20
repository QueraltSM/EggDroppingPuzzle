import functools
import sys

def memoize(f):
    cache = {}
    def newfunc(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return newfunc

@memoize
def eggDrop(eggs,floors):
    if eggs == 1 or floors < 2:
        return floors
    return min(1 + max(eggDrop(eggs - 1, x - 1), eggDrop(eggs, floors - x)) for x in xrange(1, floors))

def init(eggs,floors):
    print "- - - Memoization - - -> ", eggDrop(eggs, floors)
