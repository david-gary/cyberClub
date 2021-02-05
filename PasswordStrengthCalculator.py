# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 08:41:46 2021

@author: dgary
"""
import numpy as np

password = str(input("Type your password here: \n"))
A = int(input("How many character options does your password use? (Note: this is normally 96, 102, 105, or 107): \n"))
N = len(password)

T = (A**N)
print("\nTotal number of password possibilities: " + str(T) + "\n")
D = T/((10**9)*3600)
print("Number of years it would take a person to guess your password: " + str(D) + '\n')
X = 2*np.log2(D)
if X > 0:
    print("Number of hours it would take a computer to crack your password: " + str(X) + '\n')
else:
    print("A standard bruteforce attack can easily crack your password in under an hour.")


