class Message:
  def __init__(self, message):
    self.message = message
  def cout(self):
    print(self.message)

greeting = Message("Hello World")
greeting.cout()