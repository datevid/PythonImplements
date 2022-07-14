from SaveFile import saveFile, saveBinaryFile

if __name__ == "__main__":
    saveFile("hola mundo","saved.txt");
    saveBinaryFile(b'hola mundo',"savedBinaryFile.txt");