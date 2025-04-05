from collections import defaultdict, deque


class Solution:
    def isNeighbor(self, firstWord, secondWord):
        difference = 0
        for i in range(len(firstWord)):
            if firstWord[i] != secondWord[i]:
                difference += 1
            if difference > 1:
                return False

        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordMap = defaultdict(list)
        wordList.append(beginWord)

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.isNeighbor(wordList[i], wordList[j]):
                    wordMap[wordList[i]].append(wordList[j])
                    wordMap[wordList[j]].append(wordList[i])

        # print(wordMap)

        # since shortes path we will do a BFS traversal
        queue = deque()
        # beginWord will be the source
        queue.append((beginWord, 1))
        visited = defaultdict(bool)

        while len(queue) > 0:
            currentWord, currentDistance = queue.popleft()
            visited[currentWord] = True

            # print(currentWord)
            # print(wordMap[currentWord])

            if currentWord == endWord:
                return currentDistance

            for neighbor in wordMap[currentWord]:
                # print(neighbor)

                if not visited[neighbor]:
                    queue.append((neighbor, currentDistance + 1))

        return 0
