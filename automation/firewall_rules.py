import requests
import csv
import subprocess
import io
import time

# Constants
URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"
DELETE_RULE_TEMPLATE = "netsh advfirewall firewall delete rule name='BadIP_{direction}_{ip}'"
BLOCK_RULE_TEMPLATE = "netsh advfirewall firewall add rule name='BadIP_{direction}_{ip}' dir={direction} action=block remoteip={ip}"
MAX_RETRIES = 3
RETRY_DELAY = 2  # in seconds

def rule_updater():
    response = None
    for attempt in range(MAX_RETRIES):
        try:
            # Get data from source
            response = requests.get(URL).text
            break
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            print(f"Error occurred while trying to get data from {URL}: {e}")
            if attempt < MAX_RETRIES - 1:  # no delay on last attempt
                time.sleep(RETRY_DELAY)

    if response is None:
        print("Failed to get data after maximum retries.")
        return

    # Create separate CSV readers for outbound and inbound rules
    outbound_rules = csv.reader(filter(lambda x: not x.startswith('#'), response.splitlines()))
    inbound_rules = csv.reader(filter(lambda x: not x.startswith('#'), response.splitlines()))

    for row in outbound_rules:
        ip = row[1]
        if ip != 'dst_ip':
            print(f"Blocked outbound: {ip}")
            try:
                delete_rule = DELETE_RULE_TEMPLATE.format(direction='Out', ip=ip)
                subprocess.run(["Powershell", "-Command", delete_rule], check=True)
                block_rule = BLOCK_RULE_TEMPLATE.format(direction='Out', ip=ip)
                subprocess.run(["Powershell", "-Command", block_rule], check=True)
            except subprocess.CalledProcessError as e:
                # Handle exceptions that occur if the subprocess call fails
                print(f"Error occurred while trying to add outbound firewall rule: {e}")

    for row in inbound_rules:
        ip = row[1]
        if ip != 'dst_ip':
            print(f"Blocked inbound: {ip}")
            try:
                delete_rule = DELETE_RULE_TEMPLATE.format(direction='In', ip=ip)
                subprocess.run(["Powershell", "-Command", delete_rule], check=True)
                block_rule = BLOCK_RULE_TEMPLATE.format(direction='In', ip=ip)
                subprocess.run(["Powershell", "-Command", block_rule], check=True)
            except subprocess.CalledProcessError as e:
                # Handle exceptions that occur if the subprocess call fails
                print(f"Error occurred while trying to add inbound firewall rule: {e}")

def main():
    rule_updater()

if __name__ == '__main__':
    main()