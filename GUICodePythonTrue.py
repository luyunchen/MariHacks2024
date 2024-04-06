def display_broker_card(broker_name, broker_info):
    print("="*30)
    print(f"Broker Name: {broker_name}")
    print("-"*30)
    for attribute, value in broker_info.items():
        print(f"{attribute}: {value}")
    print("="*30)

if __name__ == "__main__":
    brokers = {}
    while True:
        broker_name = input("Enter broker name (or type 'done' to finish): ")
        if broker_name.lower() == 'done':
            break

        broker_info = {}
        while True:
            attribute = input("Enter attribute (or type 'done' to finish): ")
            if attribute.lower() == 'done':
                break
            value = input("Enter value: ")
            broker_info[attribute] = value

        brokers[broker_name] = broker_info

    for broker_name, broker_info in brokers.items():
        display_broker_card(broker_name, broker_info)


display_broker_card("BMO", "second place");