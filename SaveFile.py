def saveFile(dataString, filePath):
    # write file out
    out_file = open(filePath, "w")  # open for [w]riting as [b]inary
    out_file.write(dataString)
    out_file.close()


def saveBinaryFile(dataString, filePath):
    # write file out as binary
    out_file = open(filePath, "wb")  # open for [w]riting as [b]inary
    out_file.write(dataString)
    out_file.close()