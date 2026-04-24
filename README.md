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

#### Positive Sentiment WordCloud
![Positive WordCloud](outputs/positive_wordcloud.png)

#### Negative Sentiment WordCloud
![Negative WordCloud](outputs/negative_wordcloud.png)

### Insights
- The dataset contains four sentiment categories: **Positive, Negative, Neutral, and Irrelevant**.
- Negative sentiment dominates the dataset, followed by Positive, then Neutral, with Irrelevant being least frequent.
- Positive wordcloud highlights terms like *love, good, great, happy, excited*, showing enthusiasm around games and social media.
- Negative wordcloud emphasizes frustration with *servers, problems, time, fix, bad, shit, fuck*, reflecting complaints about technology and gaming platforms.
- Neutral and Irrelevant categories are less frequent but provide balance in sentiment distribution.

### Conclusion
This analysis demonstrates how labeled social media data can be leveraged to understand public opinion.  
- **Positive sentiments** highlight excitement and appreciation, often linked to gaming and social platforms.  
- **Negative sentiments** reveal dissatisfaction, technical issues, and strong emotional reactions.  
- Visualizations like wordclouds and distribution charts make sentiment patterns easy to interpret and communicate.  

Overall, sentiment analysis provides actionable insights into customer attitudes, helping brands and platforms identify strengths, weaknesses, and opportunities for improvement.
