import subprocess

def block_ip(ip):
    subprocess.call(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'])

def unblock_ip(ip):
    subprocess.call(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'])
