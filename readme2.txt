Bugs:

SentimentAnalyzer:
1. does not currently parse replies to comments
2. Does not work if link is part of a playlist

Todo:
1. Show (3) top comment (2) and their sentiment scores
2. Refactor, organize code into methods
	a. Better to have all actions in one method so that everything can be done in one 		loop, or separate into separate methods so that its more organized but it 		takes multiple iterations to process data?
3. Combine JSON files into 1 file (?)
4. Include youtube video name with the file
6. Sentiment scores vs. like count
7. Linear regression line in scatter plot of sentiment vs date

***wordcounts generator in plotter.py not working
   ***fix: realized that read_csv included spaces before each word (‘ the’ instead of 		‘the’)


Versions:
1.1 - changed pandas default data frame plot to a scatter plot, added line of best fit

Videos: