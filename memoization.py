import functools
import sys

def eggDrop(eggs,floors,cache):
    if eggs == 1 or floors < 2:
        return floors
    if cache.get((eggs,floors)) is not None:
        return cache[eggs,floors]
    else:
        cache[eggs,floors] = min(1 + max(eggDrop(eggs - 1, x - 1,cache), eggDrop(eggs, floors - x,cache)) for x in xrange(1, floors))
    return cache[eggs,floors]

def init(eggs,floors):
    print "Memoization = ", eggDrop(eggs, floors,{})
