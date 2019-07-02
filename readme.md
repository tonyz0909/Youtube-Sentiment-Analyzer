# Youtube Sentiment Analyzer

This project scrapes the comments off of a Youtube video and analyzes the data for:
1. comment sentiment (positive, negative, neutral, and compound scores from 0 to 1), 
	which are then organized by day.
2. most frequent words and their wordcounts (videos with more positive sentiment likely have more	
	positive words in their comments).
3. frequency of comments by month

To run the project, first run commentscraper.py with the link of the Youtube video as an additional parameter (ex. `python commentscraper.py http://youtube.com/video`). Note that you will need to obtain a YouTube API key and include it in a client-secret.json file in the main directory of the project in order to scrape comments from YouTube. It will then ask for OAuth2.0 validation. After validation, it will scrape the comments in json format into the 'comments' folder under resources, and add sentiment analysis scores to each comment (by importing sentimentAmalysis.py).
After running commentscraper, loadComments.py can be run to print a list of all the comments with their associated sentiment scores.

To see the graphical representation of the data, run plotter.py, which first plots the sentiment scores vs. date, then compound sentiment score vs. date, then frequency of comments by month, and finally most frequent words and their wordcounts. This file also uses helper files which are located under resources.

Programming Languages Used: Python

External Resources Used:
Youtube Comments API v3, Nltk Sentiment Intensity Analyzer, matplotlib, and pandas
