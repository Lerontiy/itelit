from math import sqrt
R = int(input())
ans = 0
for i in range(1, R):
    ans += int(sqrt(R*R - i*i))
ans *= 4
print(ans)
