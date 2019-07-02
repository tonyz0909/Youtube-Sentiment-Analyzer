import json
import pandas as pd
import os.path as path

# used if this file is being imported into plotter.py which is in
# a different directory
if path.isdir('resources'):
    directory = 'resources/'
else:
    directory = ''

file = directory + 'comments/comments.txt'
date_outFile = directory + 'dates/date'
day_outFile = directory + 'dates/day'
frequency_outFile = directory + 'comments/frequency'
fileNum = 0;

sentiment_dates = {}
dateP = {}
dateNeg = {}
dateNeu = {}
dateComp = {}

# dictionary that holds average data for all comments that day, not by
# individual comments
sentiment_days = {}
dayComp = {}
dayP = {}
dayNeg = {}
dayNeu = {}

# dictionary that maps the date with comment frequency
frequency = {}
freq = {}

#creates json file with dictionary of sentiment (neg, pos, etc.)
#mapped with the date and associated sentiment value
while path.isfile(file):

    data = json.load(open(file))

    items = data["items"]

    for x in range(len(items)):

        comment = items[x]["snippet"]["topLevelComment"]["snippet"]
        commentSentiment = comment["sentiment"]
        commentDate = comment["publishedAt"]

        # sentiment
        dateP[commentDate] = commentSentiment['pos']
        dateNeg[commentDate] = commentSentiment['neg']
        dateNeu[commentDate] = commentSentiment['neu']
        dateComp[commentDate] = commentSentiment['compound']

        if commentDate[:10] in dayComp.keys():
            # for each new score, average the new score with the existing
            # scores that day, taking into account how many scores have already
            # been added
            originalScore = dayComp[commentDate[:10]]['score']
            numComments = dayComp[commentDate[:10]]['numComments']
            dayComp[commentDate[:10]]['score'] = (originalScore * numComments + commentSentiment['compound']) / (numComments + 1)
            dayComp[commentDate[:10]]['numComments'] = numComments + 1

            originalScore = dayP[commentDate[:10]]['score']
            numComments = dayP[commentDate[:10]]['numComments']
            dayP[commentDate[:10]]['score'] = (originalScore * numComments + commentSentiment['compound']) / (numComments + 1)
            dayP[commentDate[:10]]['numComments'] = numComments + 1

            originalScore = dayNeg[commentDate[:10]]['score']
            numComments = dayNeg[commentDate[:10]]['numComments']
            dayNeg[commentDate[:10]]['score'] = (originalScore * numComments + commentSentiment['compound']) / (numComments + 1)
            dayNeg[commentDate[:10]]['numComments'] = numComments + 1

            originalScore = dayNeu[commentDate[:10]]['score']
            numComments = dayNeu[commentDate[:10]]['numComments']
            dayNeu[commentDate[:10]]['score'] = (originalScore * numComments + commentSentiment['compound']) / (numComments + 1)
            dayNeu[commentDate[:10]]['numComments'] = numComments + 1

        else:
            dayComp[commentDate[:10]] = {'score': commentSentiment['compound'], 'numComments': 1}
            dayP[commentDate[:10]] = {'score': commentSentiment['pos'], 'numComments': 1}
            dayNeg[commentDate[:10]] = {'score': commentSentiment['neg'], 'numComments': 1}
            dayNeu[commentDate[:10]] = {'score': commentSentiment['neu'], 'numComments': 1}

        # comment frequency (by month)
        if commentDate[:7] in freq.keys():
            freq[commentDate[:7]] = freq[commentDate[:7]] + 1
        else:
            freq[commentDate[:7]] = 1


    fileNum = fileNum + 1
    file = directory + 'comments/comments' + str(fileNum) + '.txt'

frequency['frequency'] = freq

sentiment_dates['pos'] = dateP
sentiment_dates['neg'] = dateNeg
sentiment_dates['neu'] = dateNeu
sentiment_dates['compound'] = dateComp

sentiment_days['pos'] = dayP
sentiment_days['neg'] = dayNeg
sentiment_days['neu'] = dayNeu
sentiment_days['compound'] = dayComp


with open(date_outFile + '.txt', 'w') as outfile:
        json.dump(sentiment_dates, outfile)
print("date data loaded")

with open(day_outFile + '.txt', 'w') as outfile:
        json.dump(sentiment_days, outfile)
print("date data by day loaded")

with open(frequency_outFile + '.txt', 'w') as outfile:
        json.dump(frequency, outfile)
print("comment frequency data loaded")

