import json
import operator
import os.path as path

# simple file for printing out comments in terminal

# The directory to save the comments to
directory = 'resources/comments/'

file = directory + 'comments.txt'
fileNum = 0
commentNum = 0

while path.isfile(file):
    data = json.load(open(file))

    items = data['items']

    for x in range(len(items)):
        comment = items[x]['snippet']['topLevelComment']['snippet']
        commentText = comment['textDisplay']

        commentNum = commentNum + 1
        print(str(commentNum) + '. ' + commentText)

        # print sentiment scores
        for k in sorted(comment['sentiment']):
            print('{0}: {1}, '.format(k, comment['sentiment'][k]), end='')
        print()
        print()

    fileNum = fileNum + 1
    file = directory + 'comments' + str(fileNum) + '.txt'