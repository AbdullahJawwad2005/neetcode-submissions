
class TrieNode:
    def __init__(self):
        self.characters = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.characters:
                curr.characters[ch] = TrieNode()
            curr = curr.characters[ch]
        curr.end = True        

    def search(self, word: str) -> bool:

        def DFS(index, node):
            if index == len(word):
                return node.end
            
            if word[index] == ".":
                for ch in node.characters.values():
                    if DFS(index+1, ch):
                        return True
                return False
            elif word[index] not in node.characters:
                return False

            return DFS(index+1, node.characters[word[index]])
          
        return DFS(0, self.root)
      
            
        
