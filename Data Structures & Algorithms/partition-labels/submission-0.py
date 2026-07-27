class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # PASS 1:
        # Store the last position where each character appears.
        #
        # Example: "abac"
        # last = {'a': 2, 'b': 1, 'c': 3}
        last = {}
        for i, char in enumerate(s):
            last[char] = i

        result = []

        # Start index of our current substring
        start = 0

        # Furthest position the current substring must reach
        end = 0

        # PASS 2:
        # Go through the string and determine where we can cut.
        for i, char in enumerate(s):
            # If this character appears further away than our
            # current end, we must extend the substring.
            end = max(end, last[char])

            # If we reached the furthest required position,
            # we can safely finish this substring.
            if i == end:

                # Calculate the size of the substring
                size = end - start + 1
                result.append(size)

                # The next substring starts after this one
                start = i + 1

        return result
