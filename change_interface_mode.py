import subprocess
import network_interaface

def toMonitorMode(interface):
    if interface: 
        try:
            print("Changing interace mode to Managed mode...")
            subprocess.run(["sudo", "iwconfig", interface, "mode", "monitor"])
            print("Interface mode successfully changed to Monitor mode")
        except Exception as e:
            print("Failed to put interface in Monitor mode!")
            print("Error: ", e)
    else:
        print("Selected interface is not valid!")


def toManagedMode(interface):
    if interface: 
        try:
            print("Changing interace mode to Managed mode...")
            subprocess.run(["sudo", "iwconfig", interface, "mode", "managed"])
            print("Interface mode successfully changed to Managed mode")
        except Exception as e:
            print("Failed to put interface in monitor mode!")
            print("Error: ", e)
    else:
        print("Selected interface is not valid!")


def clearTerminal():
        # Clearing terminal
    subprocess.run(["clear"]) 


if __name__ == "__main__":
    # Printing interface list
    interfaces = network_interaface.get_interfaces_list()
    network_interaface.print_interfaces()
    
    # Asking user to select interface for further operation
    selected_interface = int(input("\nSelect an interface: "))
    
    # Clears terminal
    clearTerminal()

    exit = False
    while exit != True:
        # Asking user and performing choosen function
        print("1. Put interface into monitor mode.")
        print("2. Remove interface from monitor mode.")

        selected_option = int(input("Select an interface: "))

        match (selected_option):
            case 1:
                toMonitorMode(interfaces[selected_interface])
                exit = True
            case 2:
                toManagedMode(interfaces[selected_interface])
                exit = True
            
            case default:
                print("\nPlease select a valid option.\n")