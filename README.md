# Financial News Sentiment Analysis and Stock Market Correlation
## Project Overview
This project focuses on the detailed analysis of a large corpus of financial news data to discover correlations between news sentiment and stock market movements. The challenge is designed to refine skills in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE).
## Table of Contents
- [Tasks](#tasks)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
## Tasks
### Task 2: Quantitative Analysis Using PyNance and TA-Lib
1. **Load and Prepare Data**:
   - Load stock price data into a pandas DataFrame, ensuring it includes columns like Open, High, Low, Close, and Volume.
2. **Apply Analysis Indicators with TA-Lib**:
   - Calculate various technical indicators such as moving averages, RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence).
3. **Use PyNance for Financial Metrics**:
   - Utilize PyNance to extract relevant financial metrics.
4. **Visualize the Data**:
   - Create visualizations to better understand the data and the impact of different indicators on stock prices.
### Task 3: Correlation Between News and Stock Movement
1. **Date Alignment**:
   - Ensure that both datasets (news and stock prices) are aligned by dates, potentially normalizing timestamps.
2. **Sentiment Analysis**:
   - Conduct sentiment analysis on news headlines to quantify the tone of each article using Python libraries like NLTK and TextBlob.
3. **Analysis**:
   - Calculate daily stock returns by computing the percentage change in daily closing prices.
   - Perform correlation analysis to test the correlation between daily news sentiment scores and stock returns.
## Technologies Used
- Python
- Pandas
- TA-Lib
- PyNance
- NLTK
- TextBlob
- Matplotlib/Seaborn for visualization
## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/erisimasol/Week-01-KAIM-10X.git
   cd your-Week-01-10x
