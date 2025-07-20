from user import User
class Vote:
    def __init__(self, user: User, vote_type: str):
        self.user = user
        self.type = vote_type
        # Add this line:
        if vote_type == "upvote":
            self.value = 1
        elif vote_type == "downvote":
            self.value = -1
        elif vote_type in (1, -1):
            self.value = vote_type
        else:
            raise ValueError("vote_type must be 'upvote', 'downvote', 1, or -1")
    def get_voter(self):
        return self.user

    def get_vote_type(self):
        return self.type