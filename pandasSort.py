import pandas as pd
from broker import Broker
import namegetter
import main
from collections import defaultdict
import os
import csv
import platform
# Read data from the CSV file (CHANGE IT TO YOUR DIR)
df = pd.read_csv('datasets/chix.csv', sep=';')

# Create a dictionary to store data for each broker
broker_data = defaultdict(list)

for _, row in df.iterrows():
    if pd.notnull(row['Broker']):
        broker = int(row['Broker'])
        broker_data[broker].append(row.tolist())

# Create separate CSV files for each broker
for broker, data in broker_data.items():
    companyname =   namegetter.get_company_name(int(broker))
    filename = f"{companyname}.csv"
    pd.DataFrame(data, columns=df.columns).to_csv(filename, index=False)
    print(f"Created file: {filename}")
# Create an object of class broker for each CSV file

'''
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
'''

directory = os.path.dirname(__file__)
for filename in os.listdir(directory):
    # Check if the file ends with ".csv"
    if filename.endswith('.csv'):
        # Construct the full path to the CSV file
        filepath = os.path.join(directory, filename)
        executecounter = 0
        totalcounter = 0
        highest_buy = None
        lowest_sell = None
        # Open the CSV file and read its contents
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check if the value in the 'Msg Type' column is equal to 'Add Order'
                if row['Msg Type'] == 'Order Execution':
                    # If it is, increment the counter
                    executecounter += float(row['Executed Shares'])
                if row['Msg Type'] =='Add Order':
                    totalcounter += float(row['Shares'])
                buy_sell_indicator = row.get('Buy/Sell Indicator', '')
                
                price_str = row.get('Price Decimal', '')

                if buy_sell_indicator == 'B':
                    price = float(price_str)
                    if highest_buy is None or price > highest_buy:
                        highest_buy = price
                elif buy_sell_indicator == 'S':
                    price = float(price_str)
                    if lowest_sell is None or price < lowest_sell:
                        lowest_sell = price

            if highest_buy is not None and lowest_sell is not None:
                difference = round(highest_buy - lowest_sell,5)
        print(difference)
        print(str(executecounter)+filepath)
        print(str(totalcounter)+filepath)
        bankbroker = Broker(filename.removesuffix('..csv'),totalcounter,executecounter,(executecounter/totalcounter),highest_buy,lowest_sell,difference,0)
        main.listOfBrokers.append(bankbroker)

# Define the list of column names
columns = ['Rank','Name','Overall Score', 'AddedOrder', 'ExecutedOrder', 'Ratio', 'Highest Ask', 'Lowest Bid', 'Spread']
sorted_list_of_brokers_byVolume = sorted(main.listOfBrokers, key=lambda broker: broker.get_executedOrder(), reverse = True)
sorted_list_of_brokers_byRatio = sorted(main.listOfBrokers, key=lambda broker:broker.get_ratio(), reverse = True)
sorted_list_of_brokers_bySpread = sorted(main.listOfBrokers, key=lambda broker:broker.get_spread())

list_size = len(main.listOfBrokers)*3
for index, broker in enumerate(main.listOfBrokers):
    score = list_size  # Start with the maximum possible score
    score -= sorted_list_of_brokers_byVolume.index(broker)

    score -= sorted_list_of_brokers_byRatio.index(broker)

    score -= sorted_list_of_brokers_bySpread.index(broker)
    print(score)
    broker.set_overallScore(score)
    print(broker.get_overallScore())


sorted_brokers = sorted(main.listOfBrokers, key=lambda broker: broker.get_overallScore(),reverse = True)
# Define the file name for the CSV file
csv_filename = 'datasets/brokers.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    # Write the header
    writer.writeheader()
    # Write data for each Broker object
    counteri = 0
    for broker in sorted_brokers:
        counteri+=1
        writer.writerow({'Rank':counteri,
                         'Name': broker.get_name(),
                         'Overall Score': broker.get_overallScore(),
                         'AddedOrder': broker.get_addedOrder(),
                         'ExecutedOrder': broker.get_executedOrder(),
                         'Ratio': broker.get_ratio(),
                         'Highest Ask': broker.get_highestAsk(),
                         'Lowest Bid': broker.get_lowestBid(),
                         'Spread': broker.get_spread()
                         })

relative_path = 'datasets/brokers.csv'

# Construct the absolute path to the file
absolute_path = os.path.abspath(relative_path)

# Check the platform to determine the appropriate method to open the file
if platform.system() == 'Windows':
    os.startfile(absolute_path)
elif platform.system() == 'Darwin':  # macOS
    os.system(f'open "{absolute_path}"')
elif platform.system() == 'Linux':
    os.system(f'xdg-open "{absolute_path}"')
else:
    print(f"Unsupported platform: {platform.system()}. Cannot open file.")

