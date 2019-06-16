#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:29:46 2019

@author: marcus
"""

class Store:
    def __init__(self,name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({
                'name':name,
                'price':price                
                })
    
    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
    @classmethod
    def franchise(cls, store):
        return cls(store.name+" - franchise")
    
    @staticmethod
    def store_details(store):        
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

if __name__=='__main__':
    
    store =  Store("Test")
    store2 = Store("Amazon")
    store2.add_item("Keyword", 160)
    
    Store.franchise(store)
    Store.franchise(store2)
    
    Store.store_details(store)
    Store.store_details(store2)
