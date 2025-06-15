from scapy.all import sniff, IP, TCP, UDP
from core.rule_engine import RuleEngine
from core.logger import log_packet

rule_engine = RuleEngine()

def process_packet(packet):
    if IP in packet:
        ip = packet[IP].src
        proto = "TCP" if TCP in packet else "UDP" if UDP in packet else "OTHER"
        port = packet[TCP].sport if TCP in packet else packet[UDP].sport if UDP in packet else 0

        if rule_engine.is_blocked(ip, port, proto):
            log_packet(ip, port, proto, "BLOCKED")
            print(f"[BLOCKED] {ip}:{port} ({proto})")
        else:
            log_packet(ip, port, proto, "ALLOWED")
            print(f"[ALLOWED] {ip}:{port} ({proto})")

def start_sniffing():
    sniff(prn=process_packet, store=False)
