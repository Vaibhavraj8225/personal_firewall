import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
from core.sniffer import start_sniffing

class FirewallGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Personal Firewall Monitor")
        self.log_display = ScrolledText(self.root, width=80, height=30)
        self.log_display.pack()

        self.start_btn = tk.Button(self.root, text="Start Firewall", command=self.start_sniffing)
        self.start_btn.pack()

    def update_log_display(self, message):
        self.log_display.insert(tk.END, message + "\n")
        self.log_display.see(tk.END)

    def start_sniffing(self):
        thread = threading.Thread(target=start_sniffing, daemon=True)
        thread.start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FirewallGUI()
    app.run()
