def longest_prefix(words):
  if not words:
    return " "
  prefix = words[0]
  for word in words[1:]:
    while not word.startswith(prefix):
      prefix = prefix[:-1]
      if prefix == "":
        return ""
  return prefix
print("=== Longest Common Prefix Finder ===")
print("Example Input: flower flow flight")
print("Example Input: computer compare company compact")
print("Example Input: sun sunrise sunset sunday")
print()
words = input("Enter words separated by spaces: ").split()
result = longest_prefix(words)
print(words)
print(result)