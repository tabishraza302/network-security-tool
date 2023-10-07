import subprocess
import network_interaface


if __name__ == "__main__":
    network_interfaces = network_interaface.get_interfaces()
    network_interaface.print_interfaces()

    # if network_interfaces:
    #     # print("Network Interfaces:")
    #     # print(network_interfaces[2])
    #     count = 1
    #     for interface in network_interfaces:
    #         print(f"{count}. {interface}")
    #         count + = 1
    # else:
    #     print("No network interfaces found.")