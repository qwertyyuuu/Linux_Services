import socket
import datetime

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('0.0.0.0', 1303)
    server_socket.bind(server_address)
    
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключений...")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            #print(f"Подключение от {client_address}")
            
            current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
            client_socket.send(current_time.encode('utf-8'))
            
            client_socket.close()
    except KeyboardInterrupt:
        print("Сервер остановлен")

if __name__ == "__main__":
    main()
