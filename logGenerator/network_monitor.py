import psutil
import logging
import time

# Configure logging
logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_network_stats():
    net_io = psutil.net_io_counters()
    logging.info(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")

if __name__ == "__main__":
    try:
        while True:
            log_network_stats()
            time.sleep(0.0001)
    except KeyboardInterrupt:
        print("Monitoring stopped.")