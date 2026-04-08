class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            
            for char in digitToChar[digits[i]]:
                backtracking(i + 1, curr + char)


        backtracking(0, "")
        return res