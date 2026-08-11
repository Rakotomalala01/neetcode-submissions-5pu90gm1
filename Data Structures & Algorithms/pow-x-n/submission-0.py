class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        half = self.myPow(x, n // 2)

    # Even exponent
        if n % 2 == 0:
            return half * half

        # Odd exponent
        return half * half * x