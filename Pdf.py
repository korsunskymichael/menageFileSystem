from File import File


class PdfFile(File):
    def __init__(self, name: str, content: str, whoCreated: str, description: str, fileSize: int, isWriteAble: bool):
        super().__init__(name, content, whoCreated, description, fileSize)
        self.isWriteAble = isWriteAble

    @classmethod
    def createPdf(cls,newMembers):
        """
        :param newMembers: dict with 'keys' as PdfFile attributes and 'values' as their values
        :return: PdfFile Object with the init from newMembers
        """
        return cls(newMembers.get("name"), newMembers.get("content"), newMembers.get("whoCreated"),
                   newMembers.get("description"), newMembers.get("fileSize"), newMembers.get("isWriteAble"))

    def __str__(self):
        return vars(self)

