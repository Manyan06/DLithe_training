# Trie Node
class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end = False


# Trie Class
class Trie:
  def __init__(self):
    self.root = TrieNode()

  # Insert word into trie
  def insert(self, word):
    node = self.root

    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()

        node = node.children[ch]

    node.is_end = True

  # Search word in trie
  def search(self, word):
    node = self.root

    for ch in word:
        if ch not in node.children:
            return False

        node = node.children[ch]

    return node.is_end


# Spell Checker Function
def spellChecker(trie, word):
  
  # Correct spelling
  if trie.search(word):
      print(word, "-> Correct Word")

  # Wrong spelling
  else:
      print(word, "-> Wrong Word")


# ---------------- MAIN PROGRAM ----------------

# Create Trie
trie = Trie()

# Dictionary words
words = ["apple", "banana", "cat", "dog", "hello", "python"]

# Insert words into trie
for word in words:
    trie.insert(word)

# Check spellings
spellChecker(trie, "apple")
spellChecker(trie, "banana")
spellChecker(trie, "pythn")
spellChecker(trie, "helo")
