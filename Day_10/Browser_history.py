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

  def autocomplete(self, prefix):
    def dfs(node, path, results):
      if node.is_end: results.append(path)
      for ch, nxt in node.children.items():
        dfs(nxt, path + ch, results)
    node = self.root
    for ch in prefix:
      if ch not in node.children: return []
      node = node.children[ch]
    results = []
    dfs(node, prefix, results)
    return results
  
#Example usage
history = Trie()
for url in ["facebook.com", "fast.com", "fandom.com", "google.com"]:
  history.insert(url)
print(history.autocomplete("fa"))