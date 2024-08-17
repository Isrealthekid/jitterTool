import os
import time
import re

# Function to calculate jitter
def calculate_jitter(ping_times):
    jitter = 0
    for i in range(1, len(ping_times)):
        jitter += abs(float(ping_times[i]) - float(ping_times[i-1]))
    return jitter / (len(ping_times) - 1)

# Function to ping a website and get the ping times
def ping_website():
    link = input("Enter the link you want to ping: ")
    ping_times = []
    for i in range(10):
        ping_response = os.popen(f"ping -n 1 {link}").read()
        ping_time = re.findall(r'\d+\.?\d*', ping_response)[-1]
        ping_times.append(ping_time)
    return ping_times

# Main program
if __name__ == "__main__":
    ping_times = ping_website()
    print("Sequence of ping times:")
    for i, ping_time in enumerate(ping_times):
        print(f"Ping {i+1}: {ping_time} ms")
    jitter = calculate_jitter(ping_times)
    print(f"Jitter: {jitter} ms")



