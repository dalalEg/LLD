from abc import ABC, abstractmethod
class Commentable(ABC):
    @abstractmethod
    def add_comment(self, comment):
        """Add a comment to the commentable object."""
        pass

 
    @abstractmethod
    def get_comments(self):
        """Retrieve all comments associated with the commentable object."""
        pass