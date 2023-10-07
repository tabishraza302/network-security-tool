import psutil


# Return list of interfaces with full details
def get_interfaces():
    try:
        interfaces_list_full = psutil.net_if_addrs()
        
        interfaces_name = list(interfaces_list_full.keys())

        if interfaces_name:
            first_interface = interfaces_name[0]
            del interfaces_list_full[first_interface]
        
        return interfaces_list_full
    except Exception as e:
        print(f"Error: {e}")
        return [] 


# Return list/Name of interfaces with additional details
def get_interfaces_list():
    try:
        interfaces = list(get_interfaces().keys())
        return interfaces
    except Exception as e:
        print(f"Error: {e}")
        return [] 


# Print name of interfaces
def print_interfaces():
    count = 0
    interfaces_list = get_interfaces()
    
    for interface in interfaces_list:
        print(f"{count}. {interface}")
        count += 1


# Invoked when file directly called
if  __name__ == "__main__":
    print_interfaces()


# Runs when file is invoked in import
get_interfaces()