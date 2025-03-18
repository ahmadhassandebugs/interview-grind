class TrieNode:
    def __init__(self):
        self.children = {}  # (char, node)
        self.is_end_of_a_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_a_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word): return node.is_end_of_a_word
            
            if word[idx] == ".":
                for child_node in node.children.values():
                    if dfs(child_node, idx + 1): return True
            
            if word[idx] in node.children: return dfs(node.children[word[idx]], idx + 1)
            
            return False
        return dfs(self.root, 0)

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    
    assert wd.search("pad") == False, "Test case 1 failed"
    assert wd.search("bad") == True, "Test case 2 failed"
    assert wd.search(".ad") == True, "Test case 3 failed"
    assert wd.search("b..") == True, "Test case 4 failed"
    assert wd.search("b.d") == True, "Test case 5 failed"
    assert wd.search("..d") == True, "Test case 6 failed"
    assert wd.search("...") == True, "Test case 7 failed"
    assert wd.search("....") == False, "Test case 8 failed"
    