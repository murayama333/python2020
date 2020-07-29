"""
最大公約数を求める
"""

x = int(input("X: "))
y = int(input("Y: "))

z = x
if x > y:
    z = y

gcd = 0
i = 1
while i <= z:
    if x % i == 0 and y % i == 0:
        gcd = i
    i += 1

if gcd != 0:
    print(gcd)
