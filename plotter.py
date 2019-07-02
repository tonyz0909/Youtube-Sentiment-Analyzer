import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import operator

# directory that data is located in
directory = 'resources/'

# transform data by date and sentiment ratings
import resources.dateLoader

# plot sentiment

dates = pd.read_json(directory + "dates/date.txt")
days = pd.read_json(directory + "dates/day.txt")

# extract only the dates and sentiment ratings, removing commentNum
# exclude neutral scores to prevent graph from becoming cluttered
# print(days)
for sentiment in days:
    if sentiment != 'neu':
        for date, info in days[sentiment].items():
            days[sentiment][date] = info['score']

# # print("mean sentiment score: " + str(np.mean(dates['compound'])))
dayPlot = days.plot(title='Sentiment Over Time')
dayPlot.set_xlabel('Date')
dayPlot.set_ylabel('Sentiment')
plt.show()

comp = {}
comp['compound'] = days['compound']
comp = pd.DataFrame(comp)
compPlot = comp.plot(title='Sentiment Over Time')
compPlot.set_xlabel('Date')
compPlot.set_ylabel('Sentiment')
plt.show()

# plot comment frequency by date

frequency = pd.read_json(directory + "comments/frequency.txt")
freqPlot = frequency.plot(title='Frequency of Comments by Month')
freqPlot.set_xlabel("Month")
freqPlot.set_ylabel("Number of Comments")
plt.show()



# plot wordcounts

wordCounts = json.load(open(directory + 'comments/wordCounts.txt'))

# replace meaningless words (articles, punctuation, etc.)
conditions = pd.read_csv(directory + "articles.csv", sep=" ").columns.values
wordCounts  = {i : wordCounts[i] for i in wordCounts if (i not in conditions)}

# set x coordinate of the bars
numWords = 15
x = np.arange(numWords)

sorted_words = sorted(wordCounts.items(), key=operator.itemgetter(1), reverse=True)

words = [x[0] for x in sorted_words[:numWords]]
counts = [x[1] for x in sorted_words[:numWords]]

plt.bar(x, counts)
plt.xticks(x, words)
plt.xlabel('words')
plt.ylabel('frequency')
plt.title('Most Frequently Used Words')
plt.show()