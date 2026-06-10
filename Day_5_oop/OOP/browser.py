class Browser:
  def __init__(self, homepage):
    self.current = homepage
    self.back_stack = []
    self.forward_stack = []

  def visit(self, url):
    self.back_stack.append(self.current)
    self.current = url
    self.forward_stack.clear()

  def back(self):
    if self.back_stack:
      self.forward_stack.append(self.current)
      self.current = self.back_stack.pop()
    return self.current

  def forward(self):
    if self.forward_stack:
      self.back_stack.append(self.current)
      self.current = self.forward_stack.pop()
    return self.current

  def display(self):
    print("Current page: ", self.current)

browser = Browser("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
browser.visit("leetcode.com")
browser.display()
print("Back: ",browser.back())
print("Back: ",browser.back())
print("Forward: ",browser.forward())
browser.visit("stackoverflow.com")
browser.display()
