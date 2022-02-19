import socket

	
def decryption(text):
        result = ""
        for i in range(len(text)):
                character = text[i]
                if character.isupper():
                    result += chr((ord(character) + 26 - 3 - 65) % 26 + 65)
                else:
                    result += chr((ord(character) + 26 - 3 - 97) % 26 + 97)
        return result
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(hostname)
server_port = 33333
server_address = (ip_address, 33333)
print("Starting upon PORT " + str(server_port) + " on Server: " + str(hostname))
server_socket.bind(server_address)
server_socket.listen()
while True:
    print("Waiting for connection...")
    connection, client_address = server_socket.accept()
    try:
            print("Connection from: ", client_address)
            data_received = connection.recv(1024)
            encrypted_text = data_received.decode("utf-8")
            decrypted_text_transposition = encrypted_text[::-1]
            decrypted_text_substitution = decryption(decrypted_text_transposition)
            print('Text Received: ',encrypted_text)
            print('Decryption Transposition: ', decrypted_text_transposition)
            print('Decryption Substitution (Caesar Cipher): ', decrypted_text_substitution)
            print('Decrypted Text: ', decrypted_text_substitution)
            with open('text.txt', 'w+') as file:
                file.write(decrypted_text_substitution)
            break
    finally:
            connection.close()
            break
