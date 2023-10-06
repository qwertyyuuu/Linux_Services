import socket

def main():
    server_ip = input("Введите IP адрес сервера: ")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_address = (server_ip, 1303)
        client_socket.connect(server_address)
        
        data = client_socket.recv(1024)
        
        print(f"Получено текущее время от сервера: {data.decode('utf-8')}")
        
    except ConnectionRefusedError:
        print("Ошибка: не удалось подключиться к серверу")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
