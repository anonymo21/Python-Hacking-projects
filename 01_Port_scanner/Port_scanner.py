# Port scanner using socket

import socket       # Socket module for make cliens


# Function for Scan a range of ports
def scan(HOST, start_port, end_port):
    close_ports = 0
    for port in range(start_port, end_port+1):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1.0)
        result = client.connect_ex((HOST, port))

        if result == 0:
            print(f"port {port} is open")
        else:
            close_ports +=1
            # print(f"port {port} is close/filtered")
        client.close()
    print(f"{close_ports} close port")



def main():

    print("===========Github:anonymo21===========")
    print("""╔═╗╔═╗╦═╗╔╦╗  ╔═╗╔═╗╔═╗╔╗╔╔╗╔╔═╗╦═╗
╠═╝║ ║╠╦╝ ║   ╚═╗║  ╠═╣║║║║║║║╣ ╠╦╝
╩  ╚═╝╩╚═ ╩   ╚═╝╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═""")
    print("===========Github:anonymo21===========\n")

    HOST = input("Enter Host Domain/IP : ")
    print("1. Scan a specific port")
    print("2. Scan a range of ports")
    print("3. Scan all ports")

    user_choice = int(input("Enter your choice : "))

    if user_choice == 1 :
        port_no = int(input("Enter port number : "))
        scan(HOST, port_no, port_no)
        

    elif user_choice == 2:
        start_port = int(input("Enter starting port : "))
        end_port = int(input("Enter Ending port : "))
        scan(HOST, start_port, end_port)

    elif user_choice == 3:
        ports = 65535
        scan(HOST, 1, 65536)

    else:
        print("Enter a valid input")

if __name__ == "__main__":
    main()