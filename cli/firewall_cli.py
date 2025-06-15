import sys
from core.sniffer import start_sniffing

def cli():
    print("=== CLI Firewall ===")
    print("1. Start Firewall")
    print("2. Exit")

    choice = input("Enter choice: ")
    if choice == '1':
        start_sniffing()
    else:
        sys.exit()

if __name__ == "__main__":
    cli()
