import sys
import os
import subprocess

def getPath(path):
    ppath = ""
    for i in (path[1].split("\\")[:-1]):
        ppath += i + "\\"
    return ppath

def getProjectName(path):
    return str(path[1].split("\\")[:-1][-1:]).replace("[", "").replace("]", "").replace("'", "")

def createGCCString(projectFolder):
    gccstring = 'g++ -std=c++14 '
    for i in os.listdir(projectFolder):
        if i[-3:] == 'cpp':
            gccstring += i + ' '
    gccstring += "-o "
    return gccstring

def createBatFile(projectFolder, projectName, gccstr):
    with open(f'{projectFolder}\compnrun.bat', 'w') as bat_File:
        bat_File.write('@echo off\n')
        bat_File.write(gccstr+ str(projectName)+".exe\n")
        bat_File.write(str(projectName)+'.exe\n')
        bat_File.write('pause\n')

def Main(path):
    pfolder = getPath(path) # Get the absolute path of the Project
    pname = getProjectName(path) # Get the name of the project from the name of the root folder
    createBatFile(pfolder, pname, createGCCString(pfolder)) # Create the compiler batch file
    
    subprocess.call([rf'{pfolder}\compnrun.bat'])

if __name__ == '__main__'    :
    Main(sys.argv)