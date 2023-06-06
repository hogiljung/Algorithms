def solution(phone_book):
    t = Trie()
    N = len(phone_book)
    
    for i in range(N):
        if not t.insert(phone_book[i]):
            return False
    
    for i in range(N):
        if t.search_prefix(phone_book[i]):
            return False
    
    return True
    
class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False
    
    def __init__(self):
        self.root = self.Node()
    
    def insert(self, key):
        curr_node = self.root
        for ch in key:
            if ch not in curr_node.children:
                curr_node.children[ch] = self.Node()
            if curr_node.is_end_of_word:
                return False
            curr_node = curr_node.children[ch]
        curr_node.is_end_of_word = True
        return True
        
    def search_prefix(self, key):
        curr_node = self.root
        for ch in key:
            if curr_node.is_end_of_word:
                return True
            curr_node = curr_node.children[ch]
        
        return False