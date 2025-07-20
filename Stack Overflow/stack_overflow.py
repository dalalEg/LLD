from typing import Dict
from user import User
from question import Question
from answer import Answer
from tag import Tag
from comment import Comment
from votable import Votable
from commentable import Commentable
from vote import Vote


class StackOverflow:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.questions: Dict[str, Question] = {}
        self.answers: Dict[str, Answer] = {}
        self.tags: Dict[str, Tag] = {}

    def create_user(self, username: str, email: str) -> User:
        """Create a new user."""
        if username in self.users:
            raise ValueError("Username already exists.")
        user = User(username, email)
        self.users[username] = user
        return user
    
    def ask_question(self, title: str, content: str, user: User, tags) -> Question:
        """Create a new question."""
        if not isinstance(user, User):
            raise ValueError("user must be a User instance.")
        # Convert tag names to Tag objects
        tag_objs = []
        for tag in tags:
            if isinstance(tag, Tag):
                tag_objs.append(tag)
            elif isinstance(tag, str):
                # Reuse existing Tag or create new
                if tag not in self.tags:
                    self.tags[tag] = Tag(tag)
                tag_objs.append(self.tags[tag])
            else:
                raise ValueError("Tag must be a string or Tag instance.")
        question = Question(title, content, user, tag_objs)
        user.add_question(question)
        # Store the question in the system
        self.questions[question.get_id()] = question
        return question
    
    def answer_question(self, content: str, user: User, question: Question) -> Answer:
        """Create a new answer to a question."""
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User class.")
        if not isinstance(question, Question):
            raise ValueError("Question must be an instance of Question class.")
        answer = Answer(content, user, question)
        self.answers[answer.getId()] = answer
        question.add_answer(answer)
        return answer
    
    def create_comment(self, content: str, user: User, commentable:Commentable) -> None:
        """Create a new comment on a question or answer."""
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User class.")
        if not hasattr(commentable, 'add_comment'):
            raise ValueError("Commentable must have an addComment method.")
        comment = Comment(content, user)
        commentable.add_comment(comment)

    
    def create_vote(self, user: User, votable: Votable, vote_type: str) -> Vote:
        """Create a new vote on a question or answer."""
        if not isinstance(user, User):
            raise ValueError("User must be an instance of User class.")
        if not isinstance(votable, Votable):
            raise ValueError("Votable must be an instance of Votable class.")
        if vote_type not in ['upvote', 'downvote']:
            raise ValueError("Vote type must be 'upvote' or 'downvote'.")
        vote = Vote(user, vote_type)
        votable.vote(user, vote_type)
        if vote_type == "upvote":
            user.upvote_received
        elif vote_type == "downvote":
            user.downvote_received
        return vote
    
    def accept_answer(self, question: Question, answer: Answer) -> None:
        """Accept an answer for a question."""
        if not isinstance(question, Question):
            raise ValueError("Question must be an instance of Question class.")
        if not isinstance(answer, Answer):
            raise ValueError("Answer must be an instance of Answer class.")
        if answer.getQuestion().get_id() != question.get_id():
            raise ValueError("Answer does not belong to the specified question.")
        question.accept_answer(answer)


    def get_user(self, username: str) -> User:
        """Get a user by username."""
        return self.users.get(username)
    
    def get_question(self, question_id: str) -> Question:
        """Get a question by its ID."""
        return self.questions.get(question_id)
    
    def get_answer(self, answer_id: str) -> Answer:
        """Get an answer by its ID."""
        return self.answers.get(answer_id)
    
    def searchQuestions(self, keyword: str) -> Dict[str, Question]:
        """Search questions by keyword."""
        return {qid: q for qid, q in self.questions.items() if keyword.lower() in q.get_title().lower() or keyword.lower() in q.get_body().lower()}
    
    def searchAnswers(self, keyword: str) -> Dict[str, Answer]:
        """Search answers by keyword."""
        return {aid: a for aid, a in self.answers.items() if keyword.lower() in a.getContent().lower()}
    
    def getQuestionsByTag(self, tag: str) -> Dict[str, Question]:
        """Get questions by tag name (string)."""
        return {
            qid: q
            for qid, q in self.questions.items()
            if any(t.getName() == tag for t in q.get_tags())
        }
    

    def getAnswersByUser(self, username: str) -> Dict[str, Answer]:
        """Get answers by user."""
        user = self.get_user(username)
        if not user:
            raise ValueError("User not found.")
        return {aid: a for aid, a in self.answers.items() if a.getAuthor().get_username() == username}
    

    def getQuestionsByUser(self, username: str) -> Dict[str, Question]:
        """Get questions by user."""
        user = self.get_user(username)
        if not user:
            raise ValueError("User not found.")
        return {qid: q for qid, q in self.questions.items() if q.get_author().get_username() == username}