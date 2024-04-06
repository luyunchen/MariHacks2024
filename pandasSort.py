import pandas as pd
from broker import Broker
import namegetter
import main
from collections import defaultdict
import os
import csv

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

directory = os.path.dirname(__file__)
for filename in os.listdir(directory):
    # Check if the file ends with ".csv"
    if filename.endswith('.csv'):
        # Construct the full path to the CSV file
        filepath = os.path.join(directory, filename)
        executecounter = 0
        totalcounter = 0
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
        print(str(executecounter)+filepath)
        print(str(totalcounter)+filepath)
        bankbroker = Broker(filename.removesuffix('..csv'),totalcounter,executecounter,(executecounter/totalcounter))
        main.listOfBrokers.append(bankbroker)

# Define the list of column names
columns = ['name', 'addedOrder', 'executedOrder', 'ratio']

# Define the file name for the CSV file
csv_filename = 'datasets/brokers.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    # Write the header
    writer.writeheader()
    # Write data for each Broker object
    for broker in main.listOfBrokers:
        writer.writerow({'name': broker.get_name(),
                         'addedOrder': broker.get_addedOrder(),
                         'executedOrder': broker.get_executedOrder(),
                         'ratio': broker.get_ratio()})

print(f"CSV file '{csv_filename}' has been created successfully.")
