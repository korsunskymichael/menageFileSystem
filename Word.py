from File import File


class WordFile(File):
    def __init__(self, name: str, content: str, whoCreated: str, description: str, fileSize: int):
        super().__init__(name, content, whoCreated, description, fileSize)

    @classmethod
    def createWord(cls,newMembers):
        """
        :param newMembers: dict with 'keys' as WordFile attributes and 'values' as their values
        :return: WordFile Object with the init from newMembers
        """
        return cls(newMembers.get("name"), newMembers.get("content"), newMembers.get("whoCreated"),
                   newMembers.get("description"), newMembers.get("fileSize"))

    def __str__(self):
        return vars(self)