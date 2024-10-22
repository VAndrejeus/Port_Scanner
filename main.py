import socket
import pandas as pd  # Using pandas to work with external csv file that has all port descriptions
import tkinter as tk
from datetime import datetime


# Function that opens up the ports.csv file, load up and returns the description of the ports
def port_description(port):
    port_csv = pd.read_csv("Ports.csv")
    try:
        description = port_csv.loc[port_csv['port'] == port, 'description'].values[0]
        return description
    except IndexError:
        return "Unknown service"


# Main port scanning function that uses connect_ex for exception handling
def ports_scan(ip, port_st, port_en, text_field):
    now = datetime.now()
    time_now = now.strftime("%H:%M:%S") # timestamp that is added at the beginning of the scan
    start_scan_text = f"Starting port scan on {ip} with ranges {port_start.get()}-{port_end.get()} at {time_now}...\n"
    print(start_scan_text)
    text_field.insert(tk.END, start_scan_text)
    for port in range(port_st, port_en):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.01)  #   Set time out for faster processing
        try_connect = s.connect_ex((ip, port))
        if try_connect == 0:  #   Connection to a port succeeded
            port_found_text = f" Port {port}: {port_description(port)} is open...\n"
            print(port_found_text)
            text_field.insert(tk.END, port_found_text)
            s.close()
    scan_complete_text = "SCAN COMPLETE\n"
    print(scan_complete_text)
    text_field.insert(tk.END, scan_complete_text)


def clear_field(text_field):
    text_field.delete(1.0, tk.END)


# Create main GUI window
window = tk.Tk()
window.geometry("200x400")
window.title("Port Scanner")

main_frame = tk.Frame(window)
main_frame.grid(row=0, column=0, padx=10)

# Labels
ip_label = tk.Label(main_frame, text="Enter target IP address:")
ip_label.grid(row=0, column=0, columnspan=2)
port_s_label = tk.Label(main_frame, text="Starting Port:")
port_s_label.grid(row=2, column=0)
port_e_label = tk.Label(main_frame, text="Ending Port:")
port_e_label.grid(row=2, column=1)

# Entries
ip_entry = tk.Entry(main_frame)
ip_entry.insert(0, "0.0.0.0")
ip_entry.grid(row=1, column=0, columnspan=2)

# Variables to hold port entry values
port_start = tk.IntVar()
port_end = tk.IntVar()

port_s_entry = tk.Entry(main_frame, width=5,textvariable=port_start)
port_s_entry.grid(row=3, column=0)
port_e_entry = tk.Entry(main_frame, width=5, textvariable=port_end)
port_e_entry.grid(row=3, column=1)

# Buttons
scan_button = tk.Button(main_frame, text="Start Scan", command=lambda: ports_scan(ip_entry.get(),
                                                                                  port_start.get(),
                                                                                  port_end.get(),
                                                                                  result_text))
scan_button.grid(row=4, column=0, columnspan=2)

clear_button = tk.Button(main_frame, text="Clear", command= lambda: clear_field(result_text)) # Button to clear the entry field
clear_button.grid(row=6, column=0, columnspan=2)

# Multi-line text box
result_text = tk.Text(main_frame, width=30, height=15, font=("Times New Roman", 8, "bold"))
result_text.grid(row=5, column=0, columnspan=2)


window.mainloop()

#TODO 3: Look into speeding up the scan process, multithreading.

#TODO 4: Fix any bugs associated with the scan.
