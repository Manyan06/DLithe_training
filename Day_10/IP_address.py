class TrieNode:
  def __init__(self):
    self.children, self.is_end = {}, False
class Trie:
  def __init__(self):
    self.root = TrieNode()
  def insert(self, word):
    node = self.root
    for ch in word:
      node = node.children.setdefault(ch, TrieNode())
    node.is_end = True
def longest_prefix(trie, ip):
  node, prefix, longest = trie.root, "", ""
  for ch in ip:
    if ch in node.children:
      prefix += ch
      node = node.children[ch]
      if node.is_end: longest = prefix
    else : break
  return longest

#Example
trie = Trie()
for p in ["192.168", "192.168.1", "10.0"]:
  trie.insert(p)
print(longest_prefix(trie, "192.168.1.45"))
print(longest_prefix(trie, "10.0.5.6"))
print(longest_prefix(trie, "172.16.0.1"))
trie = Trie()
for prefix in ["192.168", "192.168.1", "10.0"]:
  trie.insert(prefix)
print(longest_prefix(trie, "192.168.1.45"))