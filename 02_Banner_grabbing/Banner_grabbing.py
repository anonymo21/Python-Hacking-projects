# Banner grabber (grab service banners on open ports)

import socket

HOST = "192.168.1.4"
PORT = 22

def banner_grabbing(HOST, PORT):
    try:
       with socket.create_connection((HOST, PORT), timeout=3) as sock:
        
        data = sock.recv(4096)
        sock.close()
        return data.decode('utf-8', errors='replace').strip()
    
    except socket.timeout:
        return "Request timeout"
    except ConnectionRefusedError:
        return "Connection refuse"
    except OSError as e:
        return f"Error : {e}"


def main():
    print("==================================================")
    print("""╔╗ ╔═╗╔╗╔╔╗╔╔═╗╦═╗  ╔═╗╦═╗╔═╗╔╗ ╔╗ ╦╔╗╔╔═╗
╠╩╗╠═╣║║║║║║║╣ ╠╦╝  ║ ╦╠╦╝╠═╣╠╩╗╠╩╗║║║║║ ╦
╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═  ╚═╝╩╚═╩ ╩╚═╝╚═╝╩╝╚╝╚═╝""")
    print("=================Github:anonymo21=================\n")

    HOST = input("Enter Host domain/IP : ").strip()
    PORT = int(input("Enter port number : ").strip())

    banner = banner_grabbing(HOST, PORT)
    print(f"{HOST}, {PORT} -> {banner}")


if __name__ == "__main__":
    main()