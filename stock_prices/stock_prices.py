#!/usr/bin/python

import argparse

def find_max_profit (stock_prices):
  profit = []
  for i in range(0, len(stock_prices) - 1):
      for j in range(i + 1, len(stock_prices) - 1):
          profit.append(stock_prices[j] - stock_prices[i])
  profit.sort()
  return profit[len(profit) - 1]



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))