#!/usr/bin/python

import sys

results = 0

def making_change(amount, denominations):
  global results
  if amount == 0:
      return 1
  if amount < 0:
      return 0
  
  for i in denominations:
    results += making_change(amount - i, denominations)
    
  return results


  

  # return making_change(count + for demonimation in denominations)
  # return making_change(amount - 50, denominations) + making_change(amount - 25, denominations) + making_change(amount - 10, denominations) + making_change(amount -5, denominations) + making_change(amount - 1, denominations)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")