import json
import nltk
import operator
import os.path as path
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# directory that comment files are located in
directory = 'resources/comments/'

# add sentiment intensity scores to the json file
# tokenize comments into words and add to the arrray 'words'
def addSentiment(words):

    file = directory + 'comments.txt'
    fileNum = 0
    commentNum = 0

    sid = SentimentIntensityAnalyzer()

    while path.isfile(file):
        data = json.load(open(file))

        items = data['items']
        for x in range(len(items)):
            comment = items[x]['snippet']['topLevelComment']['snippet']
            commentText = comment['textDisplay']

            ss = sid.polarity_scores(commentText)
            comment['sentiment'] = ss

            words.extend(nltk.word_tokenize(commentText))

            commentNum = commentNum + 1

            # for k in sorted(comment['sentiment']):
            #     print('{0}: {1}, '.format(k, ss[k]), end='')
            # print()

        with open(file, 'w') as outfile:
            json.dump(data, outfile)

        fileNum = fileNum + 1
        file = directory + 'comments' + str(fileNum) + '.txt'

# create dictionary with words as keys and wordcount as values
# save into file 'wordcounts.txt' in comments folder
def wordCount(words):
    wordCount = {}

    for word in words:
        if (word in wordCount.keys()):
            wordCount[word] = wordCount[word] + 1
        else:
            wordCount[word] = 1

    with open(directory + 'wordCounts.txt', 'w') as outfile:
            json.dump(wordCount, outfile)

    # print sorted wordcount as tuples
    # sorted_words = sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_words[6:100])


words = []
addSentiment(words)
print('sentiment scores successfully added to comment files')
wordCount(words)
print('wordcounts succesfully calculated')
