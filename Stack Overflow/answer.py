from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from question import Question
from datetime import datetime
from user import User
from votable import Votable
from commentable import Commentable
from vote import Vote

class Answer(Votable, Commentable):
    def __init__(self, content, author: User, question: "Question"):
        super().__init__()
        self.id = id(self)
        self.content = content
        self.author = author
        self.question = question
        self.created_at = datetime.now()
        self.timestamp = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        self.accepted = False
        self.comments = []
        self.votes=[]
    
    def vote(self, user, value):
         # Accept both string and int for vote value
        if value == "upvote":
            value = 1
        elif value == "downvote":
            value = -1
        if value not in (1, -1):
            raise ValueError("Vote value must be either 1 or -1")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.increase_reputation(value * 10)  # +10 for upvote, -10 for downvote

    def get_vote_count(self) -> int:
        return sum(v.value for v in self.votes)

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments.copy()


    def accept(self):
        if not self.accepted:
            self.accepted = True
            self.author.increase_reputation(15)
        else:
            raise ValueError("This answer is already accepted.")
    
        

    def getId(self):
        return self.id

    def getContent(self) -> str: 
        return self.content

    def getAuthor(self):
        return self.author

    def getQuestion(self):
        return self.question

    def getTimestamp(self):
        return self.timestamp
    
    def isAccepted(self):
        return self.accepted