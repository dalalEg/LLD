from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from question import Question
    from answer import Answer
    from comment import Comment

class User:
    def __init__(self, username, email):
        self.id = id(self)
        self.username = username
        self.email = email
        self._reputation = 0
        self.questions = []
        self.answers = []
        self.comments = []

    def add_question(self, question: "Question"):
        self.questions.append(question)
        self.increase_reputation(5)  # Example reputation increase for asking a question
    
    def add_answer(self, answer: "Answer"):
        self.answers.append(answer)
        self.increase_reputation(3)  # Example reputation increase for answering a question

    def add_comment(self, comment: "Comment"):
        self.comments.append(comment)
        self.increase_reputation(2)  # Example reputation increase for commenting
        
    def increase_reputation(self, points):
        if points > 0:
            self._reputation += points
    def decrease_reputation(self, points):
        if points > 0:
            self._reputation -= points
            if self._reputation < 0:
                self._reputation = 0
    def upvote_received(self):
        self.increase_reputation(10) # Example value for upvote
    def downvote_received(self):
        self.decrease_reputation(2) # Example value for downvote    
    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_id(self):
        return self.id
    
    def get_reputation(self):       
          return self._reputation