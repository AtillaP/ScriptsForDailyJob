import sys
import time

def getProjectName(arg_path):
    pName = arg_path[:-1].split('\\') # Split the path argument along \ charachters, and put it into a list
    return pName[len(pName)-1] # Giv back the last elementof the list

def Main(file_access):
    path = file_access[1][:-20] # the second argument is the folder path,
    # where the bat file is copied
    # -20 --> amount of characters in: frontend_kickoff.bat
    
    projectname = getProjectName(path)
    #projectname = "Fos"
    
    # Create HTML file
    with open(f'{path}\index.html', 'w') as HTML_File:
        HTML_File.write('<!DOCTYPE html>\n')
        HTML_File.write('<html lang="en">\n')
        HTML_File.write('<head>\n')
        HTML_File.write('   <meta charset="UTF-8">\n')
        HTML_File.write('   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        HTML_File.write('   <meta http-equiv="X_UA_Compatible" content="ie=edge">\n')
        HTML_File.write(f'   <title>{projectname}</title>\n')
        HTML_File.write('   <link rel="stylesheet" type="text/css" href="styles.css">\n')
        HTML_File.write('   <script src="script.js" defer></script>\n')
        HTML_File.write('</head>\n')
        HTML_File.write('<body>\n\n')
        HTML_File.write('</body>\n')
        HTML_File.write('</html>')
        HTML_File.close()
    
    # Create CSS file
    with open(f'{path}\styles.css', 'w') as CSS_File:
        CSS_File.close()

    # Create JS file
    with open(f'{path}\script.js', 'w') as JS_File:
        JS_File.close()
    
    time.sleep(1)
    
if __name__ == '__main__':
    Main(sys.argv) # argument retrieved by the batch file

    
# missingFunctions = open(flist, 'r') #Opens the source, where the items need to be copied from
# functionsLookedFor = missingFunctions.readlines()
