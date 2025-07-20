from abc import ABC, abstractmethod

class Votable(ABC):
    @abstractmethod
    def vote(self, user, value):
        """Records a vote from a user with a specific value."""
        pass

    @abstractmethod
    def get_vote_count(self):
        """Returns the total count of votes."""
        pass