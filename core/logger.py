from datetime import datetime

def log_packet(ip, port, protocol, action):
    with open("logs/firewall.log", "a") as log:
        log.write(f"[{datetime.now()}] {action} - {ip}:{port} ({protocol})\n")
