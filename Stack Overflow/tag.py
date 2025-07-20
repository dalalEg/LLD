class Tag:
    def __init__(self, name: str):
        """Initialize a Tag with a name."""
        self.id=id(self)
        self.name = name
    def getId(self) -> int:
        """Return the unique identifier of the Tag."""
        return self.id
    def getName(self) -> str:
        """Return the name of the Tag."""
        return self.name