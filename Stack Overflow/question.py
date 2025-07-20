from votable  import Votable
from commentable import Commentable
from user import User
from tag import Tag
from datetime import datetime
from comment import Comment
from vote import Vote
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from answer import Answer
class Question(Votable, Commentable):
    def __init__(self, title, body, user, tags=None):
        """Initialize a Question with a title, body, user, and optional tags."""
        super().__init__()
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User class.")
        if not isinstance(title, str) or not isinstance(body, str):
            raise ValueError("Title and body must be strings.")
        if tags is not None and not all(isinstance(tag, Tag) for tag in tags):
            raise ValueError("All tags must be instances of Tag class.")
        self.id=id(self) # Unique identifier for the question
        self.title = title
        self.body = body
        self.user = user
        if tags is None:
            tags = []
        self.tags = tags
        self.answers = []
        self.comments = []
        self.votes=[]
        self.created_at = datetime.now()
        self.accepted_answer = None

    def add_answer(self, answer : "Answer"):
        """Add an answer to the question."""
        self.answers.append(answer)

    def accept_answer(self, answer : "Answer"):
        """Accept an answer to the question."""
        if answer in self.answers:
            answer.is_accepted = True
            self.accepted_answer = answer
        else:
            raise ValueError("Answer must be an instance of Answer class and part of this question's answers.")
    
    def vote(self, user, vote_type):
        """Vote on the question."""
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User class.")
        if vote_type not in ['upvote', 'downvote']:
            raise ValueError("Vote type must be 'upvote' or 'downvote'.")
        if vote_type == "upvote":
            vote_type = 1
        elif vote_type == "downvote":
            vote_type = -1
        if vote_type not in (1, -1):
            raise ValueError("Vote value must be either 1 or -1")
        #user cannot vote on their own question
        if user == self.user:
            raise ValueError("User cannot vote on their own question.")
        # Remove existing vote by the user if it exists
        vote1 = Vote(user, vote_type)
        self.votes.append(vote1)
        super().vote(user, vote_type)  # Pass user and vote_type, not Vote object

    
    def get_vote_count(self):
        return sum(v.value for v in getattr(self, 'votes', []))
    


    def add_comment(self, comment):
        """Add a comment to the question."""
        if isinstance(comment, Comment):
            self.comments.append(comment)

    def get_comments(self):
        return self.comments

    def get_answers(self)-> list:
        """Get all answers to the question."""
        return self.answers

    def get_id(self):
        return self.id
    
    def get_author(self):
        return self.user
    
    def get_title(self):
        return self.title
    
    def add_tag(self, tag):
        if isinstance(tag, Tag):
            self.tags.append(tag)

    def get_tags(self):
        return self.tags

    def get_body(self):
        return self.body
    def __str__(self):
        return f"Question(title={self.title}, body={self.body}, user={self.user})"