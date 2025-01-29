import pandas as pd
from collections import Counter
words = ' '.join(rawdata['headline']).split()
word_counts = Counter(words)
# Define a threshold for outlier detection based on word frequencies
threshold >= 5

# Identify outliers based on word frequencies
outliers = [word for word, count in word_counts.items() if count < threshold or count > 1000]
print("Outliers in text data:")
print(outliers)