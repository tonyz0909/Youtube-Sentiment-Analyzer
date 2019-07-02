import json
import operator
import re
import os.path as path

# used if this file is being imported into sentimentAnalyzer.py which is in
# a different directory
if path.isdir('resources'):
    directory = 'resources/'
else:
    directory = ''

file = directory + 'comments/comments.txt'
fileNum = 0
commentNum = 0

while path.isfile(file):
    # Read in the file
    with open(file, 'r') as fl:
      filedata = fl.read()

    # Replace the target string
    filedata = filedata.replace("&#39;", "'")
    filedata = filedata.replace("<br />", " ")
    filedata = filedata.replace("<a href=\"https://www.youtube.com/watch?v=8qitxIJAdLU&amp;t=2m16s\">", "")
    filedata = re.sub(r'</[^>]*>', '', filedata)
    filedata = re.sub(r'<[^>]*>', '', filedata)
    filedata = filedata.replace("&quot", " ")

    # Write the file out again
    with open(file, 'w') as fl:
      fl.write(filedata)

    fileNum = fileNum + 1
    file = directory + 'comments/comments' + str(fileNum) + '.txt'

print("reformat successful")