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
def worst_case_trial_count(floors, eggs):
    if eggs == 1 or floors < 2:
        return floors
    return min(1 + max(worst_case_trial_count(i - 1, eggs - 1), worst_case_trial_count(floors - i, eggs)) for i in xrange(1, floors))

if __name__ == '__main__':
    print worst_case_trial_count(10,2)
