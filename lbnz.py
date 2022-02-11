"""
Use Leibniz Formula to calculate pi
Based off the Leibniz formula for pi (see wikipedia) which states that 1-1/3+1/5-1/7+1/9-...=pi/4
Note in the algorithm k corresponds to pi/4 so we must multiply by 4 to obtain pi
"""
k = 1
s = 0
n = 1000000
for i in range(n): #Calculate the series using n number of terms
    if i % 2 == 0:#checking whether the term in the series must be added or subtracted
        s += 4/k
    else:
        s -= 4/k
    k += 2
print(s)
