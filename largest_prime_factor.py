# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import numpy as np

num = 55

largest_factor = 1
factor_array = np.array([])

for i in range(1,num):
    if num % i == 0:
        largest_factor = i
        factor_array = np.r_[factor_array,largest_factor]

print "largest factor: "
print largest_factor
print "factor_array: "
print factor_array


def recursive_prime(array):
    for x in range(2,array[-1]):

        if array[-1] % x != 0:
            largest_prime = array[-1]
            return largest_prime
        else:
            array = array[0:-1]
            recursive_prime(array)

# largest_prime

# for i in factor_list:
#     if i % range(2,i) != 0
