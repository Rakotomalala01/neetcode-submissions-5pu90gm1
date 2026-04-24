class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited =  set()
        wordSet = set(wordList)
        q = deque()
        steps = 1
        visited.add(beginWord)
        q.append(beginWord)
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft() 

                if curr == endWord:
                    return steps
                for word in wordList:
                    for idx, char in enumerate(word):
                        new_word = curr[:idx] + char + curr[idx + 1:]
                        if new_word in visited or new_word not in wordSet:
                            continue
                        visited.add(new_word)
                        q.append(new_word)
            steps += 1
            
            
        return 0
