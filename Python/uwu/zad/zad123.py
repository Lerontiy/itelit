from math import floor

someNum = int(input())
countZero = 0
m = 5

while someNum >= m:
    countZero += floor(someNum / m)
    m *= 5

print(floor(countZero))
