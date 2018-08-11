import statistics
import math
def stndev():
    n = []
    num = int(input("how many numbers: "))
    for i in range(num):
        v = int(input("Enter the element: "))
        n.append(v)
    print(n)
    b = sum(n)
    m = statistics.mean(n)
    print("the mean is:", m)            
    dev = statistics.stdev(n)
    print("the standard deviation is: ", dev)

stndev()
