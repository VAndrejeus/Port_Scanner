import socket
import pandas as pd  # Using pandas to work with external csv file that has all port descriptions


# Function that opens up the ports.csv file, load up and returns the description of the ports
def port_description(port):
    port_csv = pd.read_csv("Ports.csv")
    description = port_csv.loc[port_csv['port'] == port, 'description'].values[0]
    return description


# Main port scanning function that uses connect_ex for exception handling
def ports_scan(ip, port_start, port_end):
    print(f"Starting port scan on {ip} with ranges {port_start}-{port_end}...")
    for port in range(port_start, port_end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.01)  #   Set time out for faster processing
        try_connect = s.connect_ex((ip, port))
        if try_connect == 0:  #   Connection to a port succeeded
            print(f" Port {port}: {port_description(port)} is open...")
            s.close()


# User inputs
target_ip = input("Please enter IP you want to scan: ")
port_s = int(input("Enter the starting port: "))
port_e = int(input("Enter the ending port: "))

# main port scan function call
ports_scan(target_ip, port_s, port_e)

#TODO 1: Create Tkinter GUI.

#TODO 2: Make output print out in a GUI window.

#TODO 3: Fix any bugs associated with the scan.

#TODO 4: Look into speeding up the scan process, multithreading.