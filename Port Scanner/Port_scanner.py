import socket as sk
import termcolor

def scan_port(ip_address, port):

    with sk.socket() as sock_object:
        try:
            sock_object.connect((ip_address, port))

            print(termcolor.colored((f"Connection successful"), "green"))
            print(f"""
Connection details:
-------------------------
Port: {port}
IP Address: {ip_address}
-------------------------
""")
        
        except (ConnectionRefusedError, ConnectionError, ConnectionAbortedError, ConnectionResetError) as error:

            print(termcolor.colored((f"Connection failed"), "red"))
            print(f"""
Connection details:
-------------------------
Port: {port}
IP Address: {ip_address}
Reason: {error}
-------------------------
""")


file_path = ""
with open(file_path, "r") as ports_list:

    ip_address = ports_list.readline().strip()

    for port in ports_list:
        scan_port(ip_address, int(port.strip()))


# < ------------ NOTES ------------ >
# socket is used to communicate with other machines using TCP and UDP protocols
# termcolor is used to print statements in different colors

# with statement is used to automatically close the connection
# .close() to manually close the connection

# socket object (also known as socket descriptors)
# .connect(("<ip address>", <port>))

# Successful connection means that the port is open, otherwise the port is closed

# print(termcolor.colored(("<text>"), "<color name>"))