# sum of square difference
# Euler challenge #6

upper_bound = 101
list = range(1,upper_bound)
sum_square = 0
sum = 0

for x in list:
    square = x*x
    sum_square += square 
    print "sum_square_looping...."
    print "x: "+str(x)
    print "square: "+str(square)
    print "sum_square:"+str(sum_square)

for i in list:
    sum += i

square_sum = sum*sum

print "sum_square: "
print sum_square

print "square_sum: "
print square_sum

print "difference: "
print sum_square - square_sum
