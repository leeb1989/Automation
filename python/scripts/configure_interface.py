from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

device = {
    "device_type": "cisco_ios",
    "host": "10.0.0.1",
    "username": "lee.bartlett",
    "password": "Automation89!",
    "secret": "Automation89!",
}

try:
    with ConnectHandler(**device) as conn:
        conn.enable()

        config_commands = [
            "interface GigabitEthernet0/0/0",
            "description Uplink-to-ISP",
            "ip address 203.0.113.1 255.255.255.0",
            "no shutdown"
        ]

        output = conn.send_config_set(config_commands)
        print(output)

        # Save config (best practice)
        save_output = conn.send_command("write memory")
        print(save_output)
        

except NetmikoTimeoutException:
    print("Device unreachable")
except NetmikoAuthenticationException:
    print("Authentication failed")