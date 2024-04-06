from rich.console import Console
from rich.panel import Panel

def display_broker_card(broker_name, broker_info):
    console = Console()

    # Create a panel for broker information
    panel = Panel.fit(
        f"[bold yellow]Broker Name:[/bold yellow] {broker_name}\n"
        + "\n".join([f"[bold cyan]{attribute}:[/bold cyan] {value}" for attribute, value in broker_info.items()]),
        title="Broker Information",
        border_style="green",
        padding=(1, 2),
    )
    
    console.print(panel)

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
