'''
The Fibonacci sequence is defined by the recurrence relation:
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?:
'''
   
fib_seq = [1,1,2]
new_max = 2
while len(str(new_max)) < 1000:
    new_max = fib_seq[-2] + fib_seq[-1]
    fib_seq.append(new_max)

print "length max fib_seq: "
print len(str(max(fib_seq)))
print "length new_max: "
print len(str(new_max))

print "index: "
print fib_seq.index(new_max)

print "length fib_seq: "
print len(fib_seq)
