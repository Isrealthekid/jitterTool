import math

def calculate_jitter():
    ping_times = []
    num_pings = int(input("Enter the number of ping requests: "))

    for i in range(num_pings):
        ping_time = float(input(f"Enter ping time {i+1}: "))
        ping_times.append(ping_time)

    avg_ping_time = sum(ping_times) / num_pings
    jitter = sum(abs(pt - avg_ping_time) for pt in ping_times) / (num_pings - 1)

    print(f"Average Ping Time: {avg_ping_time} ms")
    print(f"Jitter: {jitter} ms")

calculate_jitter()