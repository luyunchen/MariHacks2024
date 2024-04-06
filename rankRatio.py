import pandas as pd

# Specify the path to your original CSV file
original_file_path = r"C:\Users\Weihan\MariHacks2024\datasets\brokers.csv"

# Load the CSV data into a DataFrame
df = pd.read_csv(original_file_path)

# Sort the DataFrame by the 'Ratio' column in descending order
df_sorted = df.sort_values('Ratio', ascending=False)

# Reset the index to get the new ranking
df_sorted = df_sorted.reset_index(drop=True)

df_sorted['Rank'] = range(1, len(df_sorted) + 1)

# Specify the path for the new CSV file
new_file_path = r"C:\Users\Weihan\MariHacks2024\datasets\rankRatio.csv"

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv(new_file_path, index=False)

print(f"New CSV file with updated ranking has been saved to: {new_file_path}")
