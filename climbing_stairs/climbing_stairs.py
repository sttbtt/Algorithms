#!/usr/bin/python

import sys

cache = {}

def climbing_stairs(n):
  if n == 1 or n == 0:
    return 1
  if n == 2:
    return 2
  if n in cache:
      return cache[n]
  else:
    val = climbing_stairs(n - 3) + climbing_stairs(n - 2) + climbing_stairs(n - 1)
    cache[n] = val
    return val







if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print()
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
    print()
  else:
    print('Usage: climbing_stairs.py [num_stairs]')