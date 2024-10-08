def calculate_jitter(ping_times):
    if len(ping_times) < 2:
        return 0.0

    delays = [ping_times[i] - ping_times[i - 1] for i in range(1, len(ping_times))]
    absolute_differences = [abs(delays[i] - delays[i - 1]) for i in range(1, len(delays))]
    jitter = sum(absolute_differences) / (len(absolute_differences))

    return jitter

def main():
    ping_times = []
    for i in range(10):
        while True:
            try:
                ping_time = float(input(f"Enter ping time for sequence {i + 1}: "))
                ping_times.append(ping_time)
                break
            except ValueError:
                print("Please enter a valid number.")

    jitter = calculate_jitter(ping_times)
    print(f"The calculated jitter is: {jitter} ms")

if __name__ == "__main__":
    main()












# def calculate_jitter(send_times, arrival_times, smoothing_factor=10):
#     if len(send_times) != len(arrival_times):
#         raise ValueError("Send times and arrival times lists must have the same length")

#     previous_jitter = 0
#     jitters = []

#     for i in range(1, len(send_times)):
#         instant_jitter = abs((arrival_times[i] - arrival_times[i - 1]) - (send_times[i] - send_times[i - 1]))
#         jitter = previous_jitter + (instant_jitter - previous_jitter) / smoothing_factor
#         jitters.append(jitter)
#         previous_jitter = jitter

#     return jitters




# def main():
#     n = int(input("Enter the number of packets: "))
#     send_times = []
#     arrival_times = []

#     print("Enter the send times:")
#     for i in range(n):
#         send_time = float(input(f"Send time for packet {i+1}: "))
#         send_times.append(send_time)

#     print("Enter the arrival times:")
#     for i in range(n):
#         arrival_time = float(input(f"Arrival time for packet {i+1}: "))
#         arrival_times.append(arrival_time)

#     jitters = calculate_jitter(send_times, arrival_times)

#     for i, jitter in enumerate(jitters, start=2):
#         print(f"Jitter for packet {i}: {jitter:.4f} ms")

# if __name__ == "__main__":
#     main()







# import subprocess

# # Get the number of packets (n) from user input
# n = int(input("Enter the number of packets to ping: "))

# # Function to ping google.com and return round trip time (RTT)
# def ping_google():
#   # Use subprocess module to execute ping command
#   ping_process = subprocess.Popen(["ping", "-c", "1", "google.com"], stdout=subprocess.PIPE)
#   output, error = ping_process.communicate()

#   # Extract RTT value from ping output (may vary depending on OS)
#   for line in output.decode("utf-8").splitlines():
#     if "time=" in line:
#       rtt = float(line.split("=")[1].split()[0])
#       return rtt

#   # Handle potential errors
#   print("Error: Unable to retrieve ping data")
#   return None

# # List to store ping round trip times
# arrival_times = []

# # Ping "google.com" n times and store RTT in arrival_times list
# for i in range(n):
#   rtt = ping_google()
#   if rtt:
#     arrival_times.append(rtt)
#   else:
#     # Handle case where ping fails
#     print(f"Ping {i+1} failed. Skipping...")

# # Check if any pings were successful
# if not arrival_times:
#   print("No successful pings. Exiting...")
#   exit()

# # Calculate average arrival time (assuming successful pings)
# average_arrival_time = sum(arrival_times) / len(arrival_times)

# # Calculate absolute deviations and jitter (AAD)
# absolute_deviations = [abs(t - average_arrival_time) for t in arrival_times]
# jitter = sum(absolute_deviations) / (len(arrival_times) - 1)

# # Print the jitter value in milliseconds (ms)
# print("Jitter (AAD):", jitter, "ms")




#
# import subprocess
#
# # Get the number of packets (n) from user input
# n = int(input("Enter the number of packets to ping: "))
#
# # Function to ping google.com and return round trip time (RTT)
# def ping_google():
#   # Use subprocess module to execute ping command
#   ping_process = subprocess.Popen(["ping", "-c", "1", "www.python.org"], stdout=subprocess.PIPE)
#   output, error = ping_process.communicate()
#
#   # Extract RTT value from ping output (may vary depending on OS)
#   for line in output.decode("utf-8").splitlines():
#     if "time=" in line:
#       rtt = float(line.split("=")[1].split()[0])
#       return rtt
#
#   # Handle potential errors
#   return None
#
# # List to store ping round trip times
# arrival_times = []
#
# # Ping "google.com" n times and store RTT in arrival_times list
# for i in range(n):
#   rtt = ping_google()
#   if rtt:
#     arrival_times.append(rtt)
#   else:
#     print(f"Ping {i+1} failed. Skipping...")
#
# # Calculate jitter (AAD) even if no successful pings (shows 0 jitter)
# if not arrival_times:
#   print("No successful pings. Jitter:", 0, "ms")
# else:
#   # Calculate average arrival time and jitter as before
#   average_arrival_time = sum(arrival_times) / len(arrival_times)
#   absolute_deviations = [abs(t - average_arrival_time) for t in arrival_times]
#   jitter = sum(absolute_deviations) / (len(arrival_times) - 1)
#   print("Jitter (AAD):", jitter, "ms")
#
#



# import subprocess
# from speedtest import Speedtest
#
# # Function to ping google.com and return round trip time (RTT)
# def ping_google():
#   # Use subprocess module to execute ping command
#   ping_process = subprocess.Popen(["ping", "-c", "1", "google.com"], stdout=subprocess.PIPE)
#   output, error = ping_process.communicate()
#
#   # Extract RTT value from ping output (may vary depending on OS)
#   for line in output.decode("utf-8").splitlines():
#     if "time=" in line:
#       rtt = float(line.split("=")[1].split()[0])
#       return rtt
#
#   # Handle potential errors
#   return None
#
# # Set a reasonable default for number of pings (can be adjusted)
# n = 10
#
# # List to store ping round trip times
# ping_times = []
#
# # Ping "google.com" n times and store RTT in ping_times list
# for i in range(n):
#   rtt = ping_google()
#   if rtt:
#     ping_times.append(rtt)
#   else:
#     print(f"Ping {i+1} failed. Skipping...")
#
# # Check if any pings were successful
# if not ping_times:
#   print("No successful pings. Exiting...")
#   exit()
#
# # Use speedtest library to get additional network information (optional)
# s = Speedtest()
# s.download()
# s.upload()
#
# print("Download speed:", s.download_speed(), "Mbps")
# print("Upload speed:", s.upload_speed(), "Mbps")
# print("Server:", s.results.server["name"])
#
# # Calculate jitter (AAD) using ping times
# average_ping = sum(ping_times) / len(ping_times)
# absolute_deviations = [abs(t - average_ping) for t in ping_times]
# jitter = sum(absolute_deviations) / (len(ping_times) - 1)
#
# # Print the jitter value in milliseconds (ms)
# print("Jitter (AAD):", jitter, "ms")




# import requests, os, sys, time
#
# def test_connection(type):
#   nullFile = os.devnull
#   with open(nullFile, "wb") as f:
#     start = time.process_time()
#     if type == 'download':
#        r = requests.get('https://httpbin.org/get', stream=True)
#     elif type == 'upload':
#        r = requests.post('https://httpbin.org/post', data={'key': 'value'})
#     else:
#        print("unknown operation")
#        raise
#
#     total_length = r.headers.get('content-length')
#     dl = 0
#
#     for chunk in r.iter_content(1024):
#         dl += len(chunk)
#         f.write(chunk)
#         done = int(30 * dl / int(total_length))
#         sys.stdout.write("\r%s: [%s%s] %s Mbps" % (type, '=' * done, ' ' * (30-done), dl//(time.process_time() - start) / 100000))
#         print('')
#
# # Example usage
# test_connection("download")
# test_connection("upload")




# import subprocess
#
# # Get the number of packets (n) from user input
# n = int(input("Enter the number of packets to ping: "))
#
# # Function to ping google.com and return round trip time (RTT)
# def ping_google():
#     try:
#         # Windows ping command
#         ping_process = subprocess.Popen(["ping", "-n", "1", "www.python.org"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         output, error = ping_process.communicate()
#
#         if ping_process.returncode != 0:
#             # Non-zero return code indicates an error
#             print(f"Ping failed with error: {error.decode('utf-8')}")
#             return None
#
#         # Extract RTT value from ping output (Windows format)
#         output = output.decode("utf-8")
#         for line in output.splitlines():
#             if "time=" in line:
#                 rtt = float(line.split("time=")[1].split("ms")[0])
#                 return rtt
#
#         # If we can't find the RTT in the output, return None
#         return None
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
#
# # List to store ping round trip times
# arrival_times = []
#
# # Ping "www.python.org" n times and store RTT in arrival_times list
# for i in range(n):
#     rtt = ping_google()
#     if rtt is not None:
#         arrival_times.append(rtt)
#     else:
#         print(f"Ping {i+1} failed. Skipping...")
#
# # Calculate jitter (AAD) even if no successful pings (shows 0 jitter)
# if not arrival_times:
#     print("No successful pings. Jitter:", 0, "ms")
# else:
#     # Calculate average arrival time and jitter as before
#     average_arrival_time = sum(arrival_times) / len(arrival_times)
#     absolute_deviations = [abs(t - average_arrival_time) for t in arrival_times]
#     jitter = sum(absolute_deviations) / len(absolute_deviations)
#     print("Jitter (AAD):", jitter, "ms")








# import os
# import time
#
# # Function to calculate jitter
# def calculate_jitter(ping_times):
#     avg_ping_time = sum(ping_times) / len(ping_times)
#     jitter = 0
#     for ping_time in ping_times:
#         jitter += abs(ping_time - avg_ping_time)
#     return jitter / len(ping_times)
#
# # Function to ping a website and get the ping times
# def ping_website():
#     link = input("Enter the link you want to ping: ")
#     ping_times = []
#     for i in range(2):
#         start_time = time.time()
#         os.system(f"ping -n 1 {link}")
#         end_time = time.time()
#         ping_times.append(end_time - start_time)
#     return ping_times
#
# # Main program
# if __name__ == "__main__":
#     ping_times = ping_website()
#     print("Sequence of ping times:")
#     for i, ping_time in enumerate(ping_times):
#         print(f"Ping {i+1}: {ping_time} seconds")
#     jitter = calculate_jitter(ping_times)
#     print(f"Jitter: {jitter} seconds")
#




# import os
# import time
#
# # Function to calculate jitter
# def calculate_jitter(ping_times):
#     jitter = 0
#     for i in range(1, len(ping_times)):
#         jitter += abs(ping_times[i] - ping_times[i-1])
#     return jitter / (len(ping_times) - 1)
#
# # Function to ping a website and get the ping times
# def ping_website():
#     link = input("Enter the link you want to ping: ")
#     ping_times = []
#     for i in range(10):
#         start_time = time.time()
#         os.system(f"ping -n 1 {link}")
#         end_time = time.time()
#         ping_times.append(end_time - start_time)
#     return ping_times
#
# # Main program
# if __name__ == "__main__":
#     ping_times = ping_website()
#     print("Sequence of ping times:")
#     for i, ping_time in enumerate(ping_times):
#         print(f"Ping {i+1}: {ping_time} seconds")
#     jitter = calculate_jitter(ping_times)
#     print(f"Jitter: {jitter} seconds")



# import os
# import time
#
# # Function to calculate jitter
# def calculate_jitter(ping_times):
#     jitter = 0
#     for i in range(1, len(ping_times)):
#         jitter += abs(ping_times[i] - ping_times[i-1])
#     return jitter / (len(ping_times) - 1)
#
# # Function to ping (link unavailable) and get the ping times
# def ping_bing():
#     ping_times = []
#     for i in range(10):
#         start_time = time.time()
#         os.system("ping -n 1 (www.google.com)")
#         end_time = time.time()
#         ping_times.append(end_time - start_time)
#     return ping_times
#
# # Main program
# if __name__ == "__main__":
#     ping_times = ping_bing()
#     print("Sequence of ping times:")
#     for i, ping_time in enumerate(ping_times):
#         print(f"Ping {i+1}: {ping_time} seconds")
#     jitter = calculate_jitter(ping_times)
#     print(f"Jitter: {jitter} seconds")