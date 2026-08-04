class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = n, n

        while fast != 1:
            slow = self.next_number(slow)
            fast = self.next_number(self.next_number(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
        return True

    def next_number(self, n):
        total = 0

        while n > 0:
            digit = n % 10          # Last digit
            total += digit * digit  # Add its square
            n //= 10                # Remove the last digit

        return total