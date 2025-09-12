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


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        queue = deque()
        queue.append((beginWord, 1))
        wordSet = set(wordList)

        while queue:
            current, distance = queue.popleft()

            if current == endWord:
                return distance

            charList = list(current)

            for i in range(len(charList)):
                for j in letters:
                    charList[i] = j
                    newWord = "".join(charList)
                    if newWord in wordSet:
                        queue.append((newWord, distance + 1))
                        wordSet.remove(newWord)

                charList = list(current)

        return 0
