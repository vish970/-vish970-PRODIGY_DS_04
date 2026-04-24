# PRODIGY_DS_04
## Task-04: Sentiment Analysis on Social Media Data
### Objective
Analyze and visualize sentiment patterns in social media data to understand public opinion and attitudes towards specific topics or brands.

### Dataset
- Source: Social media sentiment dataset (sample provided by Prodigy InfoTech)
- Contains text posts/tweets along with sentiment labels (positive, negative, neutral)

### Tools Used
- Python (Pandas, NLTK/TextBlob, Scikit-learn, Matplotlib, Seaborn, WordCloud)

### Steps
1. Load and explore the dataset.
2. Preprocess text data:
   - Remove stopwords, punctuation, and special characters.
   - Tokenize and normalize text.
   - Apply stemming/lemmatization.
3. Perform sentiment classification using libraries (TextBlob or Scikit-learn models).
4. Visualize sentiment distribution and patterns:
   - Bar chart of sentiment counts.
   - WordCloud for positive and negative sentiments.
   - Time-series or topic-based sentiment trends (if timestamps/topics available).

### Code
See `Task04.py` for full implementation.

### Visualizations
#### Sentiment Distribution
![Sentiment Distribution](outputs/sentiment_distribution.png)

#### WordCloud (Positive Sentiments)
![Positive WordCloud](outputs/positive_wordcloud.png)

#### WordCloud (Negative Sentiments)
![Negative WordCloud](outputs/negative_wordcloud.png)

### Insights
- Sentiment distribution shows whether public opinion leans positive, negative, or neutral.
- WordClouds highlight the most frequent words associated with each sentiment.
- Trends reveal how sentiment changes over time or across topics/brands.

### Conclusion
Sentiment analysis provides valuable insights into public opinion and brand perception.  
By combining text preprocessing, classification, and visualization, this task demonstrates how social media data can be leveraged to understand customer attitudes and guide business or marketing strategies.
