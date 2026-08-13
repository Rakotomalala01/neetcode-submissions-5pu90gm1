class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Anything multiplied by 0 is 0
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        # The product can have at most m + n digits
        result = [0] * (m + n)

        # Start from the rightmost digits
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Convert individual characters to digits
                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                # Multiply the two digits
                multiplication = digit1 * digit2

                # Positions where this multiplication belongs
                p1 = i + j
                p2 = i + j + 1

                # Add what may already exist at p2
                total = multiplication + result[p2]

                # Ones digit goes on the right
                result[p2] = total % 10

                # Carry goes to the left
                result[p1] += total // 10

        # Convert digits into a string
        answer = "".join(str(digit) for digit in result)

        # Remove the possible leading zero
        return answer.lstrip("0")