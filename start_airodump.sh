#!/bin/bash

# Get the first argument as the Wi-Fi interface
interface="$1"

# Start airodump-ng on the specified interface in a new GNOME Terminal window
gnome-terminal --window -- "airodump-ng $interface"