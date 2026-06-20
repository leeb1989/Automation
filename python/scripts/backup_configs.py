from netmiko import ConnectHandler
from datetime import datetime
import os

device = {
    "device_type": "cisco_ios",
    "host": "10.0.0.1",
    "username": "COTadmin",
    "password": "TableJumper48",
    "secret": "TableJumper48",
}

# Create backups directory if it doesn't exist
backup_dir = "../backups/cisco"
os.makedirs(backup_dir, exist_ok=True)

with ConnectHandler(**device) as conn:
    conn.enable()

    config = conn.send_command(
        "show running-config",
        read_timeout=120
    )

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    filename = f"{backup_dir}/{device['host']}_{timestamp}.cfg"

    with open(filename, "w") as backup:
        backup.write(config)

    print(f"Backup saved to {filename}")