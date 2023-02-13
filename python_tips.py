#Better for loops
# Tip 1:
numbers = [10,20,33,40,50,60,70,80]
result = 0
for num in numbers:
    result += num
print(result)

result = sum(numbers)
print(result) 

#Tip 2:
numbers = [10,20,33,40,50,60,70,80]
for idx, val in enumerate(numbers):
    print(idx, val)
    
#Tip 3:
a = [1,2,3]
b = ["a","b","c"]
for val1, val2 in zip(a,b):
    print(val1, val2)
#for idx1, idx2 in zip(a,b, strict=True):
#    print(idx1, idx2)

#Tip 4:
events = [("learn", 5), ("learn", 10), ("relaxed", 20)]
minutes_studied = 0
for event in events:
    if event[0] == "learn":
        minutes_studied += event[1]
print(minutes_studied)

study_times = (event[1] for event in events if event[0] == "learn")
minutes_studied = sum(study_times)
print(minutes_studied)

#Tip 5:
lines = ["line1", "line2", "line3", "line4", "line5", "line6", "line7", "line8", "line9", "line10"]
for i, line in enumerate(lines):
    if i>=5:
        break
    print(line)
print()
from itertools import islice

first_five_lines = islice(lines,5)
for line in first_five_lines:
    print(line)
    
#Tip 6:
import numpy as np

vec_a = [1,2,3]
vec_b = [4,5,6]

result = 0
for val1, val2 in zip(vec_a, vec_b):
    result += val1 * val2
print(result)

result = np.dot(vec_a, vec_b)
print(result)