from File import File


class ImageFile(File):
    def __init__(self, name: str, content: str, whoCreated: str, description: str, fileSize: int, dimensions: str):
        super().__init__(name, content, whoCreated, description, fileSize)
        self.dimensions = dimensions


    @classmethod
    def createImage(cls, newMembers):
        """
        :param newMembers: dict with 'keys' as VideoFile attributes and 'values' as their values
        :return: VideoFile Object with the init from newMembers
        """
        return cls(newMembers.get("name"), newMembers.get("content"), newMembers.get("whoCreated"),
                   newMembers.get("description"), newMembers.get("fileSize"), newMembers.get("dimensions"))

    def __str__(self):
        return vars(self)