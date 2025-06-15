import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Personal Python Firewall")
    parser.add_argument('--gui', action='store_true', help='Run GUI mode')
    parser.add_argument('--cli', action='store_true', help='Run CLI mode')
    args = parser.parse_args()

    if args.gui:
        from gui.firewall_gui import FirewallGUI
        FirewallGUI().run()
    elif args.cli:
        from cli.firewall_cli import cli
        cli()
    else:
        print("Run with --cli or --gui")
