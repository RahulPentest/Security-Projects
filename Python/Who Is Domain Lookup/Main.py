import socket as sock

def whois_lookup(domain: str):
    try:
        with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as socket:
            buffer_size = 4096
            lookup_website_address = "whois.iana.org"
            lookup_website_port = 43
            socket.connect((lookup_website_address, lookup_website_port))
            socket.send(f"{domain}\r\n".encode())

            response = socket.recv(buffer_size).decode()

            return response
    except Exception as error:
        return f"The error: {error} occurred."



# < ------------ NOTES ------------ >
# The "who is" tool is a query and response protocol used for querying large publicly available databases,
#   containing information of registered users