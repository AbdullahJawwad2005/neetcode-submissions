from collections import deque

class TrieNode:
    def __init__(self):
        self.characters = {}
        self.word= None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.characters:
                curr.characters[ch] = TrieNode()
            curr = curr.characters[ch]
        curr.word = word

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.characters:
                return False
            curr = curr.characters[ch]
        return curr.end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.insert(word)
        
        y = len(board)
        x = len(board[0])
        results = []
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def DFS(row, col, root):

            if row < 0 or row >= y or col < 0 or col >= x:
                return
            
            if board[row][col] == "#":
                return
            thing = board[row][col]
            if board[row][col] not in root.characters:
                return
            
            temp = board[row][col]
            board[row][col] = "#"
            node = root.characters[thing]
            if node.word != None:
                results.append(node.word)
                node.word = None
            
            for dr, dl in directions:
                DFS(row + dr, col + dl, node)
            
            board[row][col] = temp
                

        for row in range(y):
            for col in range(x):
                DFS(row, col, t.root)
                print(len(results))
        return results





        