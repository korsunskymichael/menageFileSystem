class File:
    def __init__(self, name: str, content: str, whoCreated: str, description: str, fileSize: int):
        self.name = name
        self.content = content
        self.whoCreated = whoCreated
        self.description = description
        self.fileSize = fileSize
