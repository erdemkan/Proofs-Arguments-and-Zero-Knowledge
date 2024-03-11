import random
import numpy
import galois

def fingerprintCalculator(_data):

    m = 128 # m is the possible characters, here we assume _data consists of ASCII values
    n = len(_data) # n is the length of the data
   
    
    p = primeChoser(m,n) # choosing our prime to work with
    GFP = galois.GF(p) # creating our prime field
    data_ascii_elements = [GFP(ord(char)) for char in _data] # a list of ASCII values of _data as field elements
    random_element = GFP(random.randint(0, p-1)) 

    sum = GFP(0)
    for i in range(len(_data)):
        sum += data_ascii_elements[i] * (random_element ** i)

    return sum, random_element

def is_prime(number): 
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

def primeChoser(m, n): # we are going to choose a prime to work with
    
    max_val = max(m, n**2) # Find the smallest prime greater than max(m, n^2)
    current = max_val + 1  # Start checking from the next number after max_val
    
    while True:
        if is_prime(current):
            return current
        current += 1

if __name__ == "__main__":

    data = "123457474774838829292929"
    fingerprint, random_element = fingerprintCalculator(data)
    print("Fingerprint:")
    print(fingerprint)
    print("random element:")
    print(random_element)
    
