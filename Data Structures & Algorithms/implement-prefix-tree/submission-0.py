

class PrefixTree:
    class TreeNode:
        def __init__(self):
            self.characters = {}
            self.end = False

    def __init__(self):
        self.root = self.TreeNode()
        
    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.characters:
                curr.characters[ch] = self.TreeNode()
            curr = curr.characters[ch]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            print(curr.end)
            if ch not in curr.characters:
                return False
            curr = curr.characters[ch]
        if curr.end == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.characters:
                return False
            curr = curr.characters[ch]
        return True
        
        