class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merged = [0, 0, 0]

        for triplet in triplets:
            if (
                triplet[0] <= target[0]
                and triplet[1] <= target[1]
                and triplet[2] <= target[2]
            ):
                for i in range(3):
                    merged[i] = max(merged[i], triplet[i])

        return merged == target