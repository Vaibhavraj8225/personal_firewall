import json

class RuleEngine:
    def __init__(self, config_path='config/rules.json'):
        with open(config_path, 'r') as file:
            self.rules = json.load(file)

    def is_blocked(self, ip, port, protocol):
        if ip in self.rules['whitelist']['ips']:
            return False

        return (
            ip in self.rules['blacklist']['ips'] or
            port in self.rules['blacklist']['ports'] or
            protocol.upper() in self.rules['blacklist']['protocols']
        )
