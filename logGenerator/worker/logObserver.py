import subprocess
import os
import signal

def start_network_monitor():
    process = subprocess.Popen(['python', 'logGenerator/network_monitor.py'])
    return process

def stop_network_monitor(process):
    os.kill(process.pid, signal.SIGTERM)

if __name__ == "__main__":
    try:
        process = start_network_monitor()
        print(f"Started network monitor with PID: {process.pid}")
        process.wait()
    except KeyboardInterrupt:
        print("Stopping network monitor...")
        stop_network_monitor(process)
        print("Network monitor stopped.")