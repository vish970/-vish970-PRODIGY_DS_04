# Task04.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv("C:/Users/Vishal.S/OneDrive/Pictures/Screenshots/prodigy internship/prodigy_DS_01/twitter_training.csv")

# Rename columns for clarity
data.columns = ["id", "entity", "sentiment", "content"]

print("Dataset shape:", data.shape)
print(data.head())

# -----------------------------
# Visualization: Sentiment Distribution
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="sentiment", data=data, palette="coolwarm")
plt.title("Sentiment Distribution")
plt.savefig("outputs/sentiment_distribution.png")
plt.close()

# -----------------------------
# WordClouds
# -----------------------------
positive_text = " ".join(data[data["sentiment"]=="Positive"]["content"].dropna().astype(str))
negative_text = " ".join(data[data["sentiment"]=="Negative"]["content"].dropna().astype(str))

# Positive WordCloud
wc_pos = WordCloud(width=800, height=400, background_color="white").generate(positive_text)
plt.figure(figsize=(10,6))
plt.imshow(wc_pos, interpolation="bilinear")
plt.axis("off")
plt.title("Positive Sentiment WordCloud")
plt.savefig("outputs/positive_wordcloud.png")
plt.close()

# Negative WordCloud
wc_neg = WordCloud(width=800, height=400, background_color="black", colormap="Reds").generate(negative_text)
plt.figure(figsize=(10,6))
plt.imshow(wc_neg, interpolation="bilinear")
plt.axis("off")
plt.title("Negative Sentiment WordCloud")
plt.savefig("outputs/negative_wordcloud.png")
plt.close()

print("Outputs saved in outputs/ folder.")
