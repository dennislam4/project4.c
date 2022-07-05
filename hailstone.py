# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/05/2022
# Description: A function that takes a positive integer parameter as the initial number of a hailstone sequence and
# returns how many steps it takes to reach 1.

def hailstone(num):
    x = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        x = x + 1
    return x