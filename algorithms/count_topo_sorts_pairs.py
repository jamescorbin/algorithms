"""
# 1359

Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.
"""

MOD = int(1e9) + 7

def call(n: int) -> int:
    if n == 1:
        ret = 1
    else:
        ret = n * (2 * n - 1) * call(n - 1)
    return ret

class Solution:
    def countOrders(self, n: int) -> int:
        return call(n) % MOD
