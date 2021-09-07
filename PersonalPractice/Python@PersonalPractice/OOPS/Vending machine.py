#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        # number of times in the machine = num_items
        # required number of coins to buy a single item = item_price
        self.num_items = num_items
        self.item_price = item_price
    def buy(self, req_items, money):
        print("number of items: ", self.num_items, " price of items", self.item_price)
        print("number of req item: ",req_items , "money there is: ", money)
        if self.num_items >= req_items:
            if self.item_price * req_items <= money:
                self.num_items -= req_items
                money -= self.item_price * req_items
                print("number of items: ", self.num_items, " price of items", self.item_price)
                print("number of req item: ",req_items , "money there is: ", money)
            else:
                print("Not enough coins")
                raise ValueError("Not enough coins")
                
        else:
            print("Not enough items in the machine")
            raise ValueError("Not enough items in the machine")
            
        return money
       
        
        
        
         
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
