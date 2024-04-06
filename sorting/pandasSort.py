import pandas as pd
from collections import defaultdict

# Read data from the CSV file(CHANGE IT TO YOUR DIR)
df = pd.read_csv('C:/Users/rayan/Desktop/chix.csv', sep=';')

# Create a dictionary to store data for each broker
broker_data = defaultdict(list)

# Iterate through the rows and extract the broker information
for _, row in df.iterrows():
    if pd.notnull(row['Broker']):
        broker = int(row['Broker'])
        broker_data[broker].append(row.tolist())

# Create separate CSV files for each broker
for broker, data in broker_data.items():
    filename = f"broker_{broker}.csv"
    pd.DataFrame(data, columns=df.columns).to_csv(filename, index=False)
    print(f"Created file: {filename}")
'''
import pandas as pd
from collections import defaultdict
import os

# Read data from the CSV file
df = pd.read_csv('C:/Users/rayan/Desktop/chix.csv', sep=';')
print(f"Loaded data: {df.shape}")

# Print the first few rows of the DataFrame
print(df.head())

# Create a dictionary to store data for each broker
broker_data = defaultdict(list)

# Create a dictionary to store order references and their status
order_status = {}

# Iterate through the rows and extract the broker information
for _, row in df.iterrows():
    order_ref = row['Order Reference']
    msg_type = row['Message Type']
    broker = row['Broker']

    # Check if the broker is a valid integer
    if pd.notnull(broker) and isinstance(broker, (int, float)):
        broker = int(broker)
    else:
        # If the broker value is empty or invalid, use a default broker ID of 0
        broker = 0

    # Check if the order is being added or canceled
    if msg_type == 'Add Order':
        # Check if the order is not already canceled
        if order_ref not in order_status or order_status[order_ref] != 'Canceled':
            broker_data[broker].append(row.tolist())
            # Mark the order as active
            order_status[order_ref] = 'Active'
            print(f"Added order {order_ref} for broker {broker}")
    elif msg_type == 'Order Cancel':
        # Check if the order is active
        if order_ref in order_status and order_status[order_ref] == 'Active':
            # Mark the order as canceled
            order_status[order_ref] = 'Canceled'
            print(f"Canceled order {order_ref}")

# Print the contents of the broker_data dictionary
print("broker_data:")
for broker, data in broker_data.items():
    print(f"Broker {broker}: {len(data)} rows")

# Print the contents of the order_status dictionary
print("order_status:")
for order_ref, status in order_status.items():
    print(f"Order {order_ref}: {status}")

# Create separate CSV files for each broker, excluding canceled orders
output_dir = "C:/Users/rayan/Desktop/broker_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")

for broker, data in broker_data.items():
    # Filter out canceled orders
    active_orders = [order for order in data if order[0] in order_status and order_status[order[0]] == 'Active']
    if active_orders:
        # Concatenate active orders for the broker
        broker_df = pd.DataFrame(active_orders, columns=df.columns)
        filename = os.path.join(output_dir, f"broker_{broker}.csv")
        broker_df.to_csv(filename, index=False)
        print(f"Saved {len(active_orders)} active orders for broker {broker} to file: {filename}")
    else:
        print(f"No active orders found for broker {broker}")

'''