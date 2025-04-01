#bro just use a modern language, instead of that 
#old boomy perl language
import socket
import random 
def random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

for i in range(101):
    response = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 80))
    ip = "87.106.67.113"
    #ip="8.8.8.8"
    request = f"GET /?{i} HTTP/1.0\r\nHost: 127.0.0.1\r\nCF-Connecting-IP: {ip}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())
    
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data.decode()
    
    # Separate headers and body
    headers, body = response.split("\r\n\r\n", 1)
    
    # Check the status code
    status_line = headers.splitlines()[0]
    status_code = int(status_line.split()[1])
    
    if status_code == 200:
        # Print the top part of the body (first 100 characters)
        print(body[:350])
    else:
        print("forbidden")
    
    s.close()