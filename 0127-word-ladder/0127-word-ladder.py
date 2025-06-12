from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque([(beginWord, 1)])
        sett = set(wordList)
        sett.discard(beginWord)

        while que:
            word, steps = que.popleft()

            if word == endWord:
                return steps
            
            for i in range(len(word)):
                original = word[i]

                for ch in range(ord('a'), ord('z') + 1):
                    word = word[:i] + chr(ch) + word[i+1:]

                    if word in sett:
                        sett.remove(word)
                        que.append((word, steps + 1))
                word = word[:i] + original + word[i+1:]
        return 0