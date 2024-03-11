import socket
import ipaddress


def check_connectivity(address):
    try:
        socket.create_connection((address, 80), timeout=5)
        return True
    except (socket.error, socket.timeout):
        return False


def is_valid_ip_address(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


def is_device_connectable(device):
    if not is_valid_ip_address(device):
        return False
    try:
        socket.create_connection((device, 80), timeout=5)
        return True
    except (socket.error, socket.timeout):
        return False


def main():
    devices = [device.strip() for device in
               input("Enter your IP addresses: ").split(',')]
    print("Checking connectivity...")
    for device in devices:
        if is_device_connectable(device):
            print(f"{device} is reachable.")
        else:
            print(f"{device} is unreachable.")


if __name__ == "__main__":
    main()
