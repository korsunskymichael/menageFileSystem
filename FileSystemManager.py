from Pdf import PdfFile
from Word import WordFile
from Video import VideoFile
from Image import ImageFile
import json

FILE_TYPES = {"Pdf": PdfFile,
              "Word": WordFile,
              "Video": VideoFile,
              "Image": ImageFile}

FILE_ENDINGS = {"pdf": "pdf",
                "word": "word",
                "png": "image",
                "jpeg": "image",
                "jpg": "image",
                "mp4": "video",
                "avi": "video"}


def createFileObject(createfile: {}):
    """
    :param createfile: a 'valid' dict: keys: members of the object
                                       values: values of the members
    :return: Object one of these following types: PdfFile, WordFile, ImageFile, VideoFile
    """
    testName = FILE_ENDINGS.get(createfile.get("name").split(".")[1])
    if testName == "word":
        return WordFile.createWord(createfile)
    elif testName == "pdf":
        return PdfFile.createPdf(createfile)
    elif testName == "video":
        return VideoFile.createVideo(createfile)
    elif testName == "image":
        return ImageFile.createImage(createfile)


class FileSystemManager():
    def __init__(self, file_name: str, maxSize: int):
        listFiles = []
        with open(file_name, "r") as f:
            listFiles = json.loads(f.read())

        print("Init list files is:")
        print(listFiles)
        print("\n")
        if maxSize < 1:
            print("maxSize: {} is less than one".format(maxSize))

        self.__maxSize = maxSize
        self.__files = []

        for file in listFiles:
            self.addFile(file)

        print("List of files that were added from the Init list files:")
        print(self.reprFiles())
        print("\n")
        print("List of files that were not added from the Init list files:")
        print([x for x in listFiles if x not in self.reprFiles()])
        print("\n")

    def checkFileValidity(self, file: {}):
        """
        :param file: a dict, potential file (dict) to be added to self.__files
        :return: boolean answer if the file (dict) is valid
        """
        countDot = 0

        # checking if the dict contain all the following keys: 'name', 'content', 'whoCreated', 'description','fileSize'
        members = ['name', 'content', 'whoCreated', 'description', 'fileSize']
        for member in members:
            if member not in file.keys():
                print("File: {} does not have member: {} in it.".format(file, member))
                return False

        # checking that all member in file are valid
        allPossibleMembers = ['name', 'content', 'whoCreated', 'description', 'fileSize',
                              'dimensions', 'isWriteAble', 'duration']
        for member in file.keys():
            if member not in allPossibleMembers:
                print("File: {} have not valid member: {}".format(file, member))
                return False

        # checking that there is only one dot in file
        for letter in str(file.get("name")):
            if letter == ".":
                countDot = countDot + 1
        if countDot != 1:
            print("File: {}. Number of dots in File name must be one.".format(file, file.get("name")))
            return False

        # checking that the ending of file is one of the following: word, pdf, avi, mp4, jpg, jpeg, png
        endingOfFile = file.get("name").split(".")[1]
        if endingOfFile not in FILE_ENDINGS.keys():
            print("File: {}. Not valid file name ending: {}. Valid endings:"
                  " word, pdf, avi, mp4, jpg, jpeg, png".format(file, endingOfFile))
            return False

        # checking that file size is not negative
        if file.get("fileSize") < 0:
            print("File: {}. File's size is a negative number: {}".
                  format(file, file.get("fileSize")))
            return False

        # checking that if file's size is 0 that the file's content have empty string
        if file.get("fileSize") == 0 and file.get("content") != "":
            print("File with file size of 0 mst have no content")
            return False

        # checking that file's size is not higher than self.__maxSize
        if file.get("fileSize") > self.maxSizeGetter():
            print("File: {}. File's size exceeds over maxSize of the system: {}".
                  format(file, self.maxSizeGetter()))
            return False

        # additional checks if the file's "type" is PdfFile
        if FILE_ENDINGS.get(endingOfFile) == "pdf":
            # file of PdfFile type must have 'isWriteAble' as its member
            if "isWriteAble" not in file.keys():
                print("File: {} with pdf ending do not have member 'isWriteAble'".format(file))
                return False
            # 'isWriteAble' must be true/false
            if (str(file.get("isWriteAble"))).lower() not in ["true", "false"]:
                print("File: {}. member 'isWriteAble' in file does not have "
                      "boolean value: {}".format(file, file.get("isWriteAble")))
                return False
            # file is valid
            else:
                return True

        # additional checks if the file's "type" is VideoFile
        if FILE_ENDINGS.get(endingOfFile) == "video":
            # file of VideoFile type must have 'duration' as its member
            if "duration" not in file.keys():
                print("File: {} with video ending do not have member 'duration'".format(file))
                return False
            # duration must be positive or equal to zero
            if int(file.get("duration")) < 0:
                print("File: {}. duration: {} must be higher or equal to zero".format(file, file.get("duration")))
                return False
            # file is valid
            else:
                return True

        # additional checks if the file's "type" is ImageFile
        if FILE_ENDINGS.get(endingOfFile) == "image":
            # a file with type ImageFile must have "dimensions" as his member
            if "dimensions" not in file.keys():
                print("File: {} with image ending do not have member 'dimensions'".format(file))
                return False
            # checking validity of the content in 'dimensions'
            if ("X" not in str(file.get("dimensions"))) or ((len(file.get("dimensions"))) < 3):
                print("File: {}. Does not have/Not valid member 'dimensions'".format(file))
                return False
            first = int(file.get("dimensions").split("X")[0])
            second = int(file.get("dimensions").split("X")[1])
            if first < 1:
                print("File: {}. left side dimension is negative".format(file))
                return False
            if second < 1:
                print("File: {}. right side dimension is negative".format(file))
                return False
            else:
                # file is valid
                return True
        # file is valid
        else:
            return True

    def maxSizeGetter(self):
        return self.__maxSize

    def filesGetter(self):
        return self.__files

    def filesSetter(self, file: {}):
        """
        :param file: a dict
        :return: file is sent to filesSetter method: file is checked by 'checkFileValidity' method for its validity if
        returned true, and file's name is not in self.__files the file sent to 'createFileObject' to create an Object which will be added to
        self.__files
        """
        if self.checkFileValidity(file):
            if file.get("name") in self.allNames():
                print("File: {}. File's Name: {} already exist in the system\n".format(file, file.get("name")))
                return False
            else:
                self.__files.append(createFileObject(file))
        else:
            print("Could not add a not valid File: {}\n".format(file))

    def reprFiles(self):
        """
        :return: list of dicts representation of self.__files
        """
        return [vars(file) for file in self.filesGetter()]

    def allNames(self):
        """
        :param
        :return: list of all file names in self.__files
        """
        allNames = []
        for names in self.getFiles().values():
            allNames.extend(names)
        return allNames

    def addFile(self, file: {}):
        """
        :param file: a dict
        :return: a valid file is added to self.__files with the help of filesSetter(file) method
        """
        self.filesSetter(file)

    def deleteFile(self, fileName: str):
        """
        :param fileName:
        :return: if fileName exist in self.__files deletes the first found (in the restriction of the project there
        should not be more than one) Object in self.__files with name equals to
        fileName
        """
        if fileName in self.allNames():
            for file in self.filesGetter():
                if file.name == fileName:
                    print("file name: {} with file type: {}, will be deleted".format(fileName, "".join(
                        [fileType for fileType in FILE_TYPES.keys() if isinstance(file, FILE_TYPES.get(fileType))])))
                    del self.filesGetter()[self.filesGetter().index(file)]
                    break
        else:
            print("File name: {} does not exist in the files".format(fileName))
            return False

    def getFiles(self, typeFile=None):
        """
        :param typeFile: must be one of the following: Pdf, Word, Video, Image or None
        :return: if typeFile is None: returns a dict with 'FILE_TYPES' keys as keys and list of names from that key in
        self.__files as their values
                 if typeFile is one of the following: Pdf, Word, Video or Image, returns a list of all files from the
                 requested typeFile
        """
        if typeFile and typeFile in FILE_TYPES.keys():
            return [file.name for file in self.filesGetter() if isinstance(file, FILE_TYPES.get(typeFile))]

        if not typeFile:
            return dict(zip(FILE_TYPES.keys(), list(map(self.getFiles, FILE_TYPES.keys()))))

        else:
            print("Wrong typeFile: {} requested. type file must be one of the following: "
                  "Pdf, Word, Video, Image".format(typeFile))
            return False

    def cloneFile(self, fileName: str, number: int):
        """
        :param fileName: fileName of one of the files in self.__files.
                         if file's type is PdfFile file.isWriteAble must be True
                         files' size must be higher than 1
        :param number: non negative int
        :return: cloning file content by number given if the cloned file's size is less or equal to self.__maxSize.
                 if type of file is 'VideoFile' also the duration is cloned
                 if type of file is 'ImageFile': the first (left) side dimension is also cloned
        """
        if fileName in self.allNames():
            if number > 0:
                for file in self.filesGetter():
                    if fileName == file.name:
                        if file.fileSize == 0:
                            print("File with file name: {} was not cloned because of file's"
                                  " size equals to 0".format(fileName))
                        else:
                            if isinstance(file, PdfFile) and not file.isWriteAble:
                                print("Can't clone file with file name: {}"
                                      " because isWriteAble equals to False".format(fileName))
                            else:
                                if file.fileSize * (number + 1) <= self.maxSizeGetter():
                                    file.content = file.content * (number + 1)
                                    file.fileSize = file.fileSize * (number + 1)
                                    if isinstance(file, VideoFile):
                                        file.duration = file.duration * (number + 1)
                                    if isinstance(file, ImageFile):
                                        file.dimensions = str((int(file.dimensions.split("X")[0])) * (number + 1)) + \
                                                          "X" + file.dimensions.split("X")[1]
                                    print("Succeeded in cloning file with file name {} by {}".format(fileName, number))
                                else:
                                    print("Can't clone file with file name: {}. File's size exceeded over maxSize: {}"
                                          " after cloning".format(fileName, self.maxSizeGetter()))
                                    return False
            else:
                print("Can't clone with less than 1. Number is given: {}".format(number))
                return False
        else:
            print("fileName: {} does not exist in the system".format(fileName))
            return False

    def concatFiles(self, file1Name, file2Name):
        """
        :param file1Name: one of the file names of files in self.__files
        :param file2Name: one of the file names of files in self.__files
        :return: both files must have the same type. adding the concatenated file from file with name equals
                 to file1Name and file with name equals to file2Name if the file size of the
                 concatenated file is less or equals to the self.__maxSize (the other two files will be
                 deleted)
        """
        newFile = {}
        if file1Name in self.allNames() and file2Name in self.allNames():
            if file1Name == file2Name:
                concatList = [file for file in self.filesGetter() if file.name == file1Name]
                concatList.extend(concatList)
            else:
                concatList = [file for file in self.filesGetter() if file.name == file1Name or file.name == file2Name]
            if isinstance(concatList[0], type(concatList[1])):
                concatenatedSize = sum([int(concatList[0].fileSize), int(concatList[1].fileSize)])
                if concatenatedSize <= self.maxSizeGetter():
                    newFile["fileSize"] = concatenatedSize
                    membersOfFile1 = vars(concatList[0])
                    membersOfFile2 = vars(concatList[1])
                    for member in membersOfFile1.keys():
                        if member == "fileSize":
                            continue
                        elif member == "duration":
                            newFile[member] = sum(
                                [int(membersOfFile1.get(member)), int(membersOfFile2.get(member))])
                        elif member == "isWriteAble":
                            newFile[member] = membersOfFile1.get(member) and membersOfFile2.get(member)
                        elif member == "dimensions":
                            newFile[member] = str(int(membersOfFile1.get(member).split("X")[0]) +
                                                  int(membersOfFile2.get(member).split("X")[0])) + "X" + \
                                              str(int(membersOfFile1.get(member).split("X")[1]) +
                                                  int(membersOfFile2.get(member).split("X")[1]))
                        elif member == "name":
                            newFile[member] = membersOfFile1.get(member).split(".")[0] + "_" + \
                                              membersOfFile2.get(member).split(".")[0] \
                                              + "." + membersOfFile1.get(member).split(".")[1]
                        elif member == 'content' and concatenatedSize == 0:
                            newFile[member] = ""
                        else:
                            newFile[member] = str(membersOfFile1[member]) + "_" + str(membersOfFile2[member])

                    self.deleteFile(file1Name)
                    if file1Name != file2Name:
                        self.deleteFile(file2Name)
                    self.addFile(newFile)
                    print("concatFiles of file name 1: {} and file name 2: {} succeeded".format(file1Name, file2Name))
                else:
                    print("concatenated file size: {} exceeds max size: {}".format(concatenatedSize,
                                                                                   self.maxSizeGetter()))
                    return False
            else:
                print("Files have no same type.")
                return False
        else:
            print("At least one of given file names: {}, {} is not in the system".format(file1Name, file2Name))
            return False

    def __str__(self):
        """
        :return: number of all files from every type in the self.__files and the self.__maxSize
        """
        return "Number of all files: {}, max size: {}". \
            format(dict(zip(FILE_TYPES.keys(), [len(group) for group in list(map(self.getFiles, FILE_TYPES.keys()))])),
                   self.maxSizeGetter())
