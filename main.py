#!/usr/bin/python3

path = './books/frankenstein.txt'

with open (path, 'r') as outfile:
    text = outfile.read()
    text = text.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    counted_items = {}
    #print(text:str)
    #print(len(text.split()))
    for item in alphabet:
        counted_letters = text.count(item)
        counted_items[item] = counted_letters
    print(counted_letters)

    for k,v in counted_items.items():
        print(f"The {k} character was found {v} times")

    
