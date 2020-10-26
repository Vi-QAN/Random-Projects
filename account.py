# -*- coding: utf-8 -*-
import csv

class Account:
    def __init__(self):
        self.MAX = 10
        self.array =  [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h%self.MAX
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for index, account in enumerate(self.array[h]):
            if len(account) == 2 and account[0] == key:
                found = True
                self.array[h][index] = (key,value)
        if not found:
            print("Account is not found")
        
    def create(self,key,value):
        h = self.get_hash(key)
        for account in self.array[h]:
            if account[0] == key:
                print("Username already existed")
        self.array[h].append((key,value))
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.array[h] is None:
            return
        for account in self.array[h]:
            if account[0] == key:
                return account[1]
            
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index, account in enumerate(self.array[h]):
            if account[0] == key:
                del self.array[h][index]
            
        
    