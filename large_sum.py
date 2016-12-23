# work out the first ten digts of the sum of the following
# one-hundred 50-digit numbers

import pandas as pd

data = pd.read_csv('large_sum_data')

tens = []

for index in range(1,len(data)):
    keep = data[index]
    keep[0]
    tens = tens.append(keep)

print tens
