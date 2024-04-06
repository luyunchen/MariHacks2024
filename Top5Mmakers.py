import os
import csv

def rank_files_by_price_difference(directory_path):
    file_price_differences = {}

    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            print("Processing file:", file_path)

            highest_buy = None
            lowest_sell = None

            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    buy_sell_indicator = row.get('Buy/Sell Indicator', '')
                    price_str = row.get('Price', '')

                    if buy_sell_indicator == 'B':
                        price = float(price_str)
                        if highest_buy is None or price > highest_buy:
                            highest_buy = price
                    elif buy_sell_indicator == 'S':
                        price = float(price_str)
                        if lowest_sell is None or price < lowest_sell:
                            lowest_sell = price

            if highest_buy is not None and lowest_sell is not None:
                difference = highest_buy - lowest_sell
                file_price_differences[file_path] = difference
            else:
                print("No buy or sell orders found in the file.")

    # Rank the files based on price differences
    ranked_files = sorted(file_price_differences.items(), key=lambda x: x[1], reverse=True)

    # Print the ranked results
    print("Ranked files by price difference:")
    for rank, (file_path, difference) in enumerate(ranked_files, start=1):
        print(f"{rank}. File: {file_path}, Price Difference: {difference}")

# Example usage
directory_path = 'C:/Users/rayan/Desktop/MariHacks2024'
rank_files_by_price_difference(directory_path)
