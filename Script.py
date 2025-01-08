
import pandas as pd
from google.colab import files

# Upload the dataset
print("Please upload the dataset:")
uploaded = files.upload()

# Load the dataset into a DataFrame
file_name = list(uploaded.keys())[0]
data = pd.read_csv(file_name)

# Defineing a placeholder for missing Trade_History
placeholder_trade_history = [{
    "timestamp": "N/A",
    "asset": "N/A",
    "side": "N/A",
    "price": 0.0,
    "quantity": 0.0,
    "realizedProfit": 0.0
}]

# Handling missing 'Trade_History' entries
data['Trade_History'] = data['Trade_History'].apply(lambda x: placeholder_trade_history if pd.isnull(x) else eval(x))

# Expanding 'Trade_History' into a DataFrame
trade_details = pd.DataFrame()
for i, row in data.iterrows():
    trades = pd.json_normalize(row['Trade_History'])
    trades['Port_IDs'] = row['Port_IDs']
    trade_details = pd.concat([trade_details, trades], ignore_index=True)

# Display the structure of 'trade_details'
print("Structure of trade_details:")
print(trade_details.info())
print(trade_details.head())

# Now proceedng with financial metric calculations
def calculate_metrics(df):
    metrics = {}
    metrics['ROI'] = (df['realizedProfit'].sum() / df['quantity'].sum()) * 100 if df['quantity'].sum() > 0 else 0
    metrics['PnL'] = df['realizedProfit'].sum()
    metrics['Sharpe_Ratio'] = df['realizedProfit'].mean() / df['realizedProfit'].std() if df['realizedProfit'].std() != 0 else 0
    metrics['MDD'] = ((df['price'].max() - df['price'].min()) / df['price'].max()) * 100 if df['price'].max() != 0 else 0
    metrics['Win_Rate'] = df[df['realizedProfit'] > 0].shape[0] / df.shape[0] if df.shape[0] > 0 else 0
    metrics['Win_Positions'] = df[df['realizedProfit'] > 0].shape[0]
    metrics['Total_Positions'] = df.shape[0]
    return pd.Series(metrics)

# Group by 'Port_IDs' and calculate metrics
metrics_df = trade_details.groupby('Port_IDs').apply(calculate_metrics)

# Rank accounts based on calculated metrics
metrics_df['Rank'] = metrics_df['ROI'].rank(ascending=False)

#  Get top 20 accounts
top_20_accounts = metrics_df.sort_values(by='Rank').head(20)

# Save results to CSV 
top_20_accounts.to_csv('top_20_accounts.csv')
# Print the top 20 accounts
print("Top 20 Accounts:")
print(top_20_accounts)
# Download the CSV file
files.download('top_20_accounts.csv'
