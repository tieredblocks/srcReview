import os
import re
import configparser

"""
This is the section where information is being retrieved from configuration file
1. Config file is present in config/config.txt file
2. Output Info will be stored in outputInfo file
"""
configParser = configparser.RawConfigParser()
configFilePath = r'../config/config.ini'
configParser.read(configFilePath)

outputFolder = configParser.get('config-params', 'outputFolder')
outputFile = configParser.get('config-params', 'outputFile')
outputInfo = configParser.get('config-params', 'outputInfo')

sourceFolder = configParser.get('config-params', 'codeDump')
fileEntry = configParser.get('config-params', 'type1')
folderEntry = configParser.get('config-params', 'type2')

debugPrint = configParser.get('config-params', 'debugPrint')

"""debug statements"""
if debugPrint == "yes":
    print("Start the debug statements")
    print("sourceFolder is: " + sourceFolder)
    sourceFolderParam = configParser.get('config-params', 'codeDumpParam')
    outputDir = configParser.get('config-params', 'outputDir')
    print("Source Code Param is : " + sourceFolderParam)
    print("Output Directory is :" + outputDir)
    print("outputInfo is: " + outputFolder)
    print("output file is " + outputFile)
    print("complete file path is " + outputFolder + outputFile)
    print("fileEntry is: " + fileEntry)
    print(folderEntry)

outputCSV = open(outputInfo, "w")

folderArr = [sourceFolder]
baseLevel = len(re.findall("/", sourceFolder))
dirLevel = 0

"""
Old Source Code put here
sourceCSVFile = open("/home/madhup/Documents/dev/folderInfo.csv" , "w")
outputCSV = ""
sourceFolder = "/home/madhup/Documents/postgre/postgresql-12.3"
fileEntry = "file"
folderEntry = "folder"

folderArr=[sourceFolder]
baseLevel = len(re.findall("/", sourceFolder))
dirLevel = 0

"""




"""
This is the function which will create the CSV File with all the entries in the source folder
1. Serial Number of all the entries
2. Folder Level, which is equivalent to folder depth. 
3. Type, which is either file or folder
4. Parent Folder of the entry
5. Entry, which is either the file name or folder name

The task is done in the following steps
1. It writes the header to the CSV file, which has been defined at the program level
2. It iterates through the base folder array of the source code
3. It iterates through all the entries present in the base folder array
4. If the entry is a folder, then the folder gets added to the base folder array at end of the list
5. It makes an entry to the CSV file based on the header information that has been defined in step 1.
"""


def inputSrcInfo (folderPath):
    outerCount = 0
    entryCount = 0
    newEntry = ""
    subDirCount = 0
    folderLevel = 0
    folderAdded = False

    """
    outputCSV.write("Sl" + "\t" + "Level" + "\t" + "Type" + "\t" + "Parent Folder" + "\t" + "Curr File" + "\n")
    Changed the variable name
    sourceCSVFile.write("Sl" + "\t" + "Level" + "\t" + "Type" + "\t" + "Parent Folder" + "\t" + "Curr File" + "\n")
    """

    outputCSV.write("Sl" + "\t" + "Level" + "\t" + "Type" + "\t" + "Parent Folder" + "\t" + "Curr File" + "\n")

    while outerCount < len(folderArr):
        folderList = os.listdir(folderArr[outerCount])

        parentFolder = folderArr[outerCount]
        debugStr = "Folder Array Len is {}. Folder Name in outer count is {}.\n Sub Dir Count is {}. Folder Level is {}."
        
        outerCount += 1
        newEntry = ""

        dirLevel = len(re.findall("/",parentFolder))
        folderLevel = dirLevel - baseLevel

        print(debugStr.format(len(folderArr), parentFolder, subDirCount, folderLevel))

        for entry in folderList:
            childEntry = parentFolder + "/" + entry
            entryCount += 1
            
            newEntry = str(entryCount) + "\t" + str(folderLevel) +"\t"

            if (os.path.isdir(childEntry)):
                folderArr.append(childEntry)
                newEntry += folderEntry + "\t" + parentFolder + "\t" + entry + "\n"
                subDirCount += 1
                outputCSV.write(newEntry)
            else:
                newEntry += fileEntry + "\t" + parentFolder + "\t" + entry + "\n"
                outputCSV.write(newEntry)



inputSrcInfo(sourceFolder)