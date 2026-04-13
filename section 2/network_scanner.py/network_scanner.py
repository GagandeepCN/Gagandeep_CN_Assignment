import socket
import time

# Function to scan a port
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))
    
    if result == 0:
        return "OPEN"
    else:
        return "CLOSED"

# Main program
def main():
    print("==== Network Scanner ====")

    target_ip = input("Enter Target IP: ")
    ports = input("Enter ports (comma separated, e.g. 21,22,80): ")

    # Convert ports to list
    port_list = [int(p) for p in ports.split(",")]

    # Start time
    start_time = time.time()

    # Open file to save results
    file = open("scan_results.txt", "w")

    print("\nScanning...\n")

    for port in port_list:
        status = scan_port(target_ip, port)
        result = f"Port {port}: {status}"
        
        print(result)
        file.write(result + "\n")

    file.close()

    # End time
    end_time = time.time()

    print("\nScan Completed!")
    print(f"Time taken: {round(end_time - start_time, 2)} seconds")

if __name__ == "__main__":
    main()
