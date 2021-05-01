from FileSystemManager import FileSystemManager

if __name__ == '__main__':

	print(
	    "---------------------------------tests---------------------------------"
	)

	print(
	    "-----------------------init of FileSystemManager2----------------------"
	)
	fileSystemManager2 = FileSystemManager("files.txt", -3)
	print("fileSystemManager2 was initiated:")
	print(fileSystemManager2)
	print("\n")

	print(
	    "-----------------------init of FileSystemManager-----------------------"
	)
	fileSystemManager = FileSystemManager("files.txt", 100)
	print("fileSystemManager was initiated:")
	print(fileSystemManager)
	print("\n")

	print(
	    "----------------------------addFile function---------------------------"
	)

	#Valid files:
	fileDict1 = {
	    "name": "file1_1.avi",
	    "content": "first video file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 10,
	    "duration": 40
	}

	fileDict2 = {
	    "name": "file2_1.avi",
	    "content": "first video file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 15,
	    "duration": 60
	}

	fileDict3 = {
	    "name": "file2_1.word",
	    "content": "third word file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 15
	}

	fileDict4 = {
	    "name": "file2_2.word",
	    "content": "third word file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 75
	}
	fileDict5 = {
	    "name": "file57.jpg",
	    "content": "bla bla",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 10,
	    "dimensions": "15X12"
	}

	fileDict6 = {
	    "name": "file52.jpg",
	    "content": "bla bla",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 27,
	    "dimensions": "7X3"
	}

	fileDict7 = {
	    "name": "file52.png",
	    "content": "bla bla",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 33,
	    "dimensions": "18X3"
	}

	fileDict8 = {
	    "name": "file52.jpeg",
	    "content": "bla bla",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 95,
	    "dimensions": "18X18"
	}

	fileDict9 = {
	    "name": "file8.pdf",
	    "content": "pdf file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 15,
	    "isWriteAble": True
	}

	fileDict10 = {
	    "name": "file9.pdf",
	    "content": "pdf file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 15,
	    "isWriteAble": False
	}

	fileDict11 = {
	    "name": "file12.pdf",
	    "content": "pdf file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 45,
	    "isWriteAble": True
	}

	fileDict12 = {
	    "name": "file11.pdf",
	    "content": "",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 0,
	    "isWriteAble": True
	}

	print("Trying to add 12 valid files to fileSystemManager:")
	fileSystemManager.addFile(fileDict1)
	fileSystemManager.addFile(fileDict2)
	fileSystemManager.addFile(fileDict3)
	fileSystemManager.addFile(fileDict4)
	fileSystemManager.addFile(fileDict5)
	fileSystemManager.addFile(fileDict6)
	fileSystemManager.addFile(fileDict7)
	fileSystemManager.addFile(fileDict8)
	fileSystemManager.addFile(fileDict9)
	fileSystemManager.addFile(fileDict10)
	fileSystemManager.addFile(fileDict11)
	fileSystemManager.addFile(fileDict12)
	print(fileSystemManager)
	print("\n")

	#list of not valid files
	print("Trying to add list of not valid files:")
	errorFileList = [{
	    "name": "file6.pdf",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": -5,
	    "isWriteAble": True
	}, {
	    "name": "file7.pdf",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 14,
	    "isWriteAble": True
	}, {
	    "name": "file8.pdf",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 14,
	    "isWriteAble": "test"
	}, {
	    "name": "file9.pdf",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 14
	}, {
	    "name": "file3.word",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 105
	}, {
	    "name": "file1.jpg",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "bla bla",
	    "fileSize": 10
	}, {
	    "name": "file2.jpg",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "bla bla",
	    "fileSize": 10,
	    "dimensions": "-5X10"
	}, {
	    "name": "file3.avi",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 10,
	    "duration": -2
	}, {
	    "name": "file4.avi",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 10
	}, {
	    "name": "file2.mp4",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 7,
	    "duration": 10
	}, {
	    "name": "file2.mp4",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 0,
	    "duration": 10
	}, {
	    "name": "file2.mp4",
	    "content": "error file",
	    "whoCreated": "michael",
	    "description": "",
	    "fileSize": 5,
	    "duration": 10
	}]

	for errorFile in errorFileList:
		fileSystemManager.addFile(errorFile)
	print("\n")
	print("Current state:")
	print(fileSystemManager)
	print("\n")

	print(
	    "---------------------------getFiles function---------------------------"
	)
	print("Trying to get the name of all files in fileSystemManager:")
	allFiles = fileSystemManager.getFiles()
	print(allFiles)
	print("\n")
	print("Return of only the names of pdf files:")
	allPdfFiles = fileSystemManager.getFiles("Pdf")
	print(allPdfFiles)
	print("\n")
	print("Return only the names of word files:")
	allWordFiles = fileSystemManager.getFiles("Word")
	print(allWordFiles)
	print("\n")
	print("Return only the names of image files:")
	allImageFiles = fileSystemManager.getFiles("Image")
	print(allImageFiles)
	print("\n")
	print("Return only the names of video files:")
	allVideoFiles = fileSystemManager.getFiles("Video")
	print(allVideoFiles)
	print("\n")
	print(
	    "Trying to return a wrong type file: Example (not one of: Pdf, Word, Image, Video)"
	)
	allExampleFiles = fileSystemManager.getFiles("Example")
	print(allExampleFiles)
	print("\n")
	print(
	    "Trying to return a wrong type file: word (not one of: Pdf, Word, Image, Video)"
	)
	lowerWordFiles = fileSystemManager.getFiles("word")
	print(lowerWordFiles)
	print("\n")
	print(
	    "Trying to return a wrong type file: pdf (not one of: Pdf, Word, Image, Video)"
	)
	lowerPdfFiles = fileSystemManager.getFiles("pdf")
	print(lowerPdfFiles)
	print("\n")
	print("Current state of fileSystemManager:")
	print(fileSystemManager)
	print("\n")

	print(
	    "---------------------------cloneFile function----------------------------"
	)
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file7.pdf' by 25:")
	fileSystemManager.cloneFile("file7.pdf", 25)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file7.pdf' by 5:")
	fileSystemManager.cloneFile("file7.pdf", 5)
	print("\n")
	print("Current state:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file2_2.word' by 0:")
	fileSystemManager.cloneFile("file7.pdf", 0)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file2_2.word' by 1:")
	fileSystemManager.cloneFile("file7.pdf", 1)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file157.word' by 7:")
	fileSystemManager.cloneFile("file157.word", 7)
	print("\n")
	print("Current state of files in fileSystemManager")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file1_1.avi' by 3:")
	fileSystemManager.cloneFile("file1_1.avi", 3)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file2.mp4' by 2:")
	fileSystemManager.cloneFile("file2.mp4", 2)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file5658.mp4' by 2:")
	fileSystemManager.cloneFile("file5658.mp4", 2)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file11.pdf' by 2:")
	fileSystemManager.cloneFile("file11.pdf", 2)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file9.pdf' by 2:")
	fileSystemManager.cloneFile("file9.pdf", 2)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file52.jpeg' by 3:")
	fileSystemManager.cloneFile("file52.jpeg", 3)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print("Trying to clone file with name 'file57.jpg' by 3:")
	fileSystemManager.cloneFile("file57.jpg", 3)
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(fileSystemManager)
	print("\n")

	print(
	    "--------------------------deleteFile function----------------------------"
	)
	fileNamesToDelete = [
	    "file541.pdf", "file7.pdf", "file1_1.avi", "file57.jpg", "file2.word",
	    "file2.word", "file2.mp4", "file2.word", "file57.jpg"
	]
	print("Trying to delete files with the file names from fileNamesToDelete:")
	print(fileNamesToDelete)
	print("\n")
	for fileName in fileNamesToDelete:
		fileSystemManager.deleteFile(fileName)
		print("Current state of fileSystemManager:")
		print(fileSystemManager)
		print("All file names in fileSystemManager:")
		print(fileSystemManager.getFiles())
		print("\n")
	print("\n")

	print(
	    "--------------------------concatFiles function---------------------------"
	)
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'testfile' and file with name: 'file8.pdf':"
	)
	fileSystemManager.concatFiles("testfile", "file8.pdf")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file8.pdf' and file with name: 'file52.jpeg':"
	)
	fileSystemManager.concatFiles("file8.pdf", "file52.jpeg")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file1.word' and file with name: 'file52.jpeg':"
	)
	fileSystemManager.concatFiles("file1.word", "file52.jpeg")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file52.jpeg' and file with name: 'file52.jpeg':"
	)
	fileSystemManager.concatFiles("file52.jpeg", "file52.jpeg")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file52.jpeg' and file with name: 'file52.jpg':"
	)
	fileSystemManager.concatFiles("file52.jpeg", "file52.jpg")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file52.jpg' and file with name: 'file52.png':"
	)
	fileSystemManager.concatFiles("file52.jpg", "file52.png")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file9.pdf' and file with name: 'file8.pdf':"
	)
	fileSystemManager.concatFiles("file9.pdf", "file8.pdf")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file8_file9.pdf' and file with name: 'file12.pdf':"
	)
	fileSystemManager.concatFiles("file8_file9.pdf", "file12.pdf")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file2_1.word' and file with name: 'file2_2.word':"
	)
	fileSystemManager.concatFiles("file2_1.word", "file2_2.word")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file2.avi' and file with name: 'file1.avi':"
	)
	fileSystemManager.concatFiles("file2.avi", "file1.avi")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file1.word' and file with name: 'file1.word':"
	)
	fileSystemManager.concatFiles("file1.word", "file1.word")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file2_1_file2_2.word' and file with name: 'file1_file1.word':"
	)
	fileSystemManager.concatFiles("file2_1_file2_2.word", "file1_file1.word")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "Trying to concatFiles: file with name: 'file11.pdf' and file with name: 'file11.pdf':"
	)
	fileSystemManager.concatFiles("file11.pdf", "file11.pdf")
	print("\n")
	print("Current state of files in fileSystemManager:")
	for file in fileSystemManager.reprFiles():
		print(file)
	print("\n")
	print(
	    "------------------------------end of tests-------------------------------"
	)
	print("After all tests state of fileSystemManager:")
	print(fileSystemManager)
