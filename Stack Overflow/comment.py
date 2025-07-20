from datetime import datetime
class Comment:
    def __init__(self, content, author):
        self.id =id(self)
        self.content = content
        self.author = author
        self.created_at = datetime.now()
    def getId(self):
        return self.id
    def getContent(self):
        return self.content
    def getAuthor(self):
        return self.author
    def getTimestamp(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")
    