class TextEditor:
  def __init__(self):
    self.text = ""
    self.undo_stack = []
    self.redo_stack = []

  def add_text(self, new_text):
    self.undo_stack.append(self.text)
    self.text += new_text
    self.redo_stack.clear()

  def undo(self):
    if self.undo_stack:
      self.redo_stack.append(self.text)
      self.text = self.undo_stack.pop()

  def redo(self):
    if self.redo_stack:
      self.undo_stack.append(self.text)
      self.text = self.redo_stack.pop()

  def display(self):
    print("Current Text: ", self.text)

editor = TextEditor()
editor.add_text("Hello")
editor.add_text(" World")
editor.display()
editor.undo()
editor.display()
editor.redo()
editor.display()