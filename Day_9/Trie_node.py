class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False
class Trie:
  def __init__(self):
    self.root = TrieNode()
  def insert(self, word):
    node = self.root
    for char in word:
      node = node.children.setdefault(char, TrieNode())
    node.is_end_of_word = True
  def search(self, word):
    node = self.root
    for char in word:
      node = node.children.get(char)
      if not node:
        return False
    return node.is_end_of_word

class SpellChecker:
  def __init__(self, dictionary):
    self.trie = Trie()
    for word in dictionary:
      self.trie.insert(word)
  def check(self, word):
    return self.trie.search(word)
  
dictionary = ["hello", "world", "python", "program"]
checker = SpellChecker(dictionary)
print(checker.check("hello"))
print(checker.check("java"))