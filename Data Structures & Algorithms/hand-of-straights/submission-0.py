class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        for num in sorted(counter):
            if counter[num] == 0:
                continue
            need = counter[num]
            for nxt in range(num, num + groupSize):
                if counter[nxt]< need:
                    return False
                counter[nxt] -= need
        return True