Assignment Report: Analysis of Binance Accounts' Trade Data

Objective
The task was to analyze historical trade data from Binance accounts to calculate key financial metrics, rank the accounts based on their performance, and identify the top 20 accounts from the past 20 dayes.

• Overview:
The provided Python code performs a series of steps to achieve the task's objective, using the `pandas` library in a Google Colab environment. I used goggle colab in making this project.



Steps Followed:

• Step 1: Uploading the Dataset
The script prompts the user to upload a CSV file and reads it into a Pandas DataFrame.

• Step 2: Handling Missing Data
  - A placeholder trade entry is defined to replace any missing or null `Trade_History` entries.
  - The `eval` function was used to convert string representations of lists to actual lists for further processing.

• Step 3: Expanding Trade History
  - The `Trade_History` JSON entries were expanded into a detailed DataFrame using `pd.json_normalize`.
  - Each trade entry was associated with its respective `Port_IDs`.

Step 4: Displaying Trade Details
-  The script uses `DataFrame.info()` and `DataFrame.head()` to show the structure and content of the expanded trade details DataFrame.

• Step 5: Calculating Financial Metrics
  - Metrics like ROI, PnL, Sharpe Ratio, Maximum Drawdown (MDD), Win Rate, Win Positions, and Total Positions were computed using custom logic.
  - A function `calculate_metrics` was defined to apply these calculations to each group of trades.

• Step 6: Grouping and Calculating Metrics
-  The `groupby` method was used to group the data by `Port_IDs`, and the `apply` method was used to apply the `calculate_metrics` function to each group.

• Step 7: Ranking Accounts
  - Accounts were ranked based on ROI using the `rank` method.
  - Accounts with higher ROI received better ranks (lower rank numbers).

• Step 8: Identifying Top 20 Accounts
-  The script sorted the DataFrame by rank and selected the top 20 accounts using the `head` method.

• Step 9: Saving Results
- The top 20 accounts were saved to a CSV file named `top_20_accounts.csv` using the `to_csv` method.

• Step 10: Downloading the CSV File
-  The Colab `files.download()` function was used to enable the download of the CSV file.


• Key Metrics Explained:
1. ROI (Return on Invstment): A measure of the profitability of the investments made by the accounts.
2. PnL (Profit and Loss): The net gain or loss from trades from last 20 days.
3. Sharpe Ratio: A risk-adjusted return metric, comparing the mean of realized profits to their standard deviation.
4. Maximum Drawdown (MDD): The largest loss from a peak to a trough in the account's trade value.
5. Win Rate: The ratio of profitable trades to the total number of trades.
6. Win Positions: The total number of profitable trades.
7. Total Positions: The total number of trades executed.


Summary of Results:
- Top 20 Accounts: The accounts with the highest ROI were identified and listed.
- Rankings: Accounts were ranked based on their ROI, with additional insights into their profitability and risk profiles.


Conclusion:
The script successfully analyzed the Binance accounts' trade data,
calculated essential financial metrics, and identified the top-performing accounts. 
This analysis provides valuable insights into the trading performance of different accounts,
highlighting those with the best return on investment and risk-adjusted returns. 
The comprehensive approach ensures that both profitability and risk are considered in the ranking of accounts.
though I used some ai assistance on fixing the issues and definition of the logics.
