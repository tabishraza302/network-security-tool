# import subprocess
# import time

# # def get_process_info(pid):
# #     try:
# #         # Run the 'tasklist' command to get process information by PID
# #         command = f"tasklist /FI \"PID eq {pid}\""
# #         process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# #         output, _ = process.communicate()

# #         # Print the process information
# #         print(output)
# #     except Exception as e:
# #         print("Error:", e)


# def capture_airodump_output():
#     try:
#         # Execute the shell script and pass the interface as an argument
#         shell_script = "./start_airodump.sh"  # Replace with the actual path to your script
#         process = subprocess.Popen([shell_script, "wlan0"], shell=True, text=True)
        
#         # Capture the PID of the GNOME Terminal
#         terminal_pid = process.pid
#         print(f"GNOME Terminal PID: {terminal_pid}")

#         # Wait for the user to press Enter (for demonstration purposes)
#         input("Press Enter to continue...")

#         # Optionally, you can interact with or control the terminal here if needed

#     except Exception as e:
#         print("Error:", e)

#     # try:
#     #     interface = "wlan0"
#     #     output_file = "scanned_networks"
        
#     #     # Run airodump-ng and redirect its output to a file
#     #     # command = f"gnome-terminal -- airodump-ng --output-format csv -w {output_file} {interface}"
#     #     # scanning_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, text=True)
#     #     # command = f"gnome-terminal -- airodump-ng --output-format csv -w {output_file} {interface}"
#     #     scanning_process = subprocess.Popen(["airodump-ng", "wlan0"]).pid

#     #     print(scanning_process)
#     #     # get_process_info(scanning_process.pid)
#     #     # output = subprocess.run(["tasklist", "/FI", "\"PID eq", scanning_process.pid, "\ "])
#     #     # print(output)
#     #     # Now, you can read the captured output from the file
#     #     # with open(output_file, "r") as file:
#     #     #     output = file.read()
        
#     #     # # Print the captured output
#     #     # print(output)
#     # except Exception as e:
#     #     print("Error:", e)

# capture_airodump_output()


import subprocess
import os
import time
import readchar
import threading

        # Listen for key presses in a separate thread
def key_event_listener():
    try:
        print("Press a key (Ctrl+C to exit):")
        while True:
            key = readchar.readchar()
            print(f"You pressed: {key}")
    except Exception as e:
        print("\nExiting key event listener...")

     # Start the key event listener in a separate thread
key_listener_thread = threading.Thread(target=key_event_listener)
key_listener_thread.start()

def start_gnome_terminal():
    try:
        # Start a GNOME Terminal
        terminal_process = subprocess.Popen(["gnome-terminal"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for a few seconds (for demonstration purposes)
        # time.sleep(5)
        key_event_listener()
        

        # Capture the PID of the GNOME Terminal
        terminal_pid = terminal_process.pid
        print(f"GNOME Terminal PID: {terminal_pid}")

        # Optionally, you can interact with or control the terminal here if needed

    except Exception as e:
        print("Error:", e)

start_gnome_terminal()
