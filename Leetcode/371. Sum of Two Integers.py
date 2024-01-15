class Solution:
    def getSum(self, a: int, b: int):
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask #^ is exclusive OR
        return a if a <= MAX else ~(a ^ mask)