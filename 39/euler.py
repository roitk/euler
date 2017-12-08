import sys
import math
from collections import defaultdict
from timeit import default_timer

def triangle_inequality(a, b, c):
    return a + b > c and b + c > a and a + c > b

## Conditions for success:
# 1. Sides satisfy triangle inequality
# 2. Sides satisfy Pythagorean theorem
def check_valid_sides(a, b, c):
    c2 = pow(a, 2) + pow(b, 2)
    return triangle_inequality(a, b, c) and c2 == pow(c, 2)

def find_num_lengths(p):
    total = 0
    valid_configs = defaultdict(lambda: False)
    for a in range(1, p):
        for b in range(1, p - a):
            if(valid_configs[(a, b)] or valid_configs[(b, a)]):
                continue
            c = p - a - b
            if c <= 0:
                continue
            if check_valid_sides(a, b, c):
                total = total + 1
                valid_configs[(a, b)] = True
    return total

def main(lo, hi):
    start_time = default_timer()
    old_total = 0
    old_p = -1
    for p in range(int(lo), int(hi)+1):
        if p % 2 != 0:
            continue
        total = find_num_lengths(p)
        if total > old_total:
            old_total = total
            old_p = p
    end_time = default_timer()
    total_time = end_time - start_time
    print "%d: %d" % (old_p, old_total)
    print "execution time: %.5f" % total_time

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print "usage: python euler.py lo hi"
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
