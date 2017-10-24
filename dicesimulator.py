#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:10:37 2017

@author: vaghanideep
"""

import random
min = 1
max = 6

roll_again = "Y"

while roll_again == "Y" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = ("Wanna roll them again?")