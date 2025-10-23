# message_tree.py
# Defines the MessageNode class for discussion threads (Tree structure)

class MessageNode:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.replies = []
