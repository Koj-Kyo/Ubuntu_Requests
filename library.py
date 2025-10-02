# Challenge: Use popular Python libraries to perform useful tasks!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. Create a NumPy array of numbers from 1 to 10 and calculate the mean.
arr = np.arange(1, 11)
mean_val = np.mean(arr)
print("NumPy array:", arr)
print("Mean:", mean_val)

# 2. Load a small dataset into a pandas DataFrame and display summary statistics.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Score': [88, 92, 95, 85]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary statistics:\n", df.describe())

# 3. Fetch data from a public API using requests and print a key piece of information.
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_rate = bitcoin_data['bpi']['USD']['rate']
    print("\nCurrent Bitcoin Price in USD:", usd_rate)
else:
    print("\nFailed to fetch Bitcoin price.")

# 4. Plot a simple line graph using matplotlib (e.g., a list of numbers).
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
plt.plot(numbers, marker='o')
plt.title("Simple Line Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

