import math

#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def divisor(larger,smaller):
    while smaller != 0:
        return divisor(smaller, larger%smaller)
    else:
        return larger


#Exercise 2
#Write a function that returns prime numbers less than 121

def primeLess(highest):
    for number in range(1,highest):
        if all(number%index != 0 for index in range(2,number)):
            print number


#Another way...
primeLister=[]
def primeLesser(highest):
    for number in range(2,highest+1):
        if number in range(2, number+1):
            primeLister.append(number)
            print number
    
#Another another way...
def primes(number, divisible=2):
    if divisible > number/2.0: 
        return True
    elif number%divisible==0: 
        return False
    else:
        divisible+=1
        return primes(number,divisible)


def primesAgain(maximum):
    for i in range(until):
        if primes(i):
            print i





#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html





