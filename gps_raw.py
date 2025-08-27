import socket

HOST = "0.0.0.0"  
PORT = 5055        
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Listening for Teltonika GPS on {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"\n📡 Connection from {addr}")
    
    data = conn.recv(4096)
    if not data:
        continue

    # Print raw formats
    print("Raw BYTES:", data)
    print("Raw HEX  :", data.hex())

    # Important → send ACK back so device continues sending
    conn.send(b'\x00\x00\x00\x01')
    conn.close()
