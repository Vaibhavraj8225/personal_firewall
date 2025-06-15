<p align="center">
  <img src="https://img.shields.io/github/license/your-username/personal_firewall?style=flat-square">
  <img src="https://img.shields.io/github/languages/top/your-username/personal_firewall?style=flat-square">
  <img src="https://img.shields.io/github/issues/your-username/personal_firewall?style=flat-square">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/placeholder/firewall-banner.png" alt="Firewall Banner" width="600"/>
</p>

## 📄 License
This project is licensed under a [Custom Permissive License](LICENSE) © 2025 Vaibhav Raj Sahu.

# 🛡️ Python Personal Firewall

A lightweight Python-based personal firewall that:
- Sniffs incoming/outgoing traffic using Scapy
- Applies custom rules to block/allow IPs, ports, and protocols
- Logs suspicious packets
- Optionally uses iptables for system-level enforcement
- Offers CLI for live monitoring

## 🚀 Features
- Custom rule engine (IP, port, protocol based)
- Logging and auditing
- GUI with real-time packet display
- CLI monitoring
- Integration with iptables (Linux only)

## 📦 Installation
```bash
git clone https://github.com/Vaibhavraj8225/personal_firewall.git
cd personal_firewall
pip install -r requirements.txt

⚙️ Usage
Run in CLI mode:
```bash
sudo python3 main.py --cli
