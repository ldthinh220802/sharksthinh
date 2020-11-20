# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:06:51 2020

@author: Acer
"""

import getpass
#initialize
flag = False
while not flag:
    u = input("Username: ")
    p = getpass.getpass(prompt="Password: ")
    flag = u == "peter" and p == "Rj@is2019"
    if flag:
        print("You logged into the system.")
    else:
        print("Either username or password is wrong.")
        ch = input("Do you want to continue? (y/n)")
        flag = ch == "N" or ch == "n"
         #out of loop
print("Finished!")