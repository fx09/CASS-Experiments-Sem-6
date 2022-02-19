import socket


def encryption(text):
    result = ""
    for i in range(len(text)):
        character = text[i]
        if character.isupper():
            result += chr((ord(character) + 3 - 65) % 26 + 65)
        else:
            result += chr((ord(character) + 3 - 97) % 26 + 97)
    return result


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
server_address = (ip_address, 33333)
client_socket.connect(server_address)
file_text = input('Enter the text for the file you wish to encrypt: ')
with open('text.txt', 'w+') as file:
        file.write(file_text)
result_substitution = encryption(file_text)
print('result_substitution = ', result_substitution)
# transposition
result_transposition = result_substitution[::-1]
print('result_transposition = ', result_transposition)
with open('text.txt', 'w+') as file:
        file.write(result_transposition)
data_to_send = result_transposition.encode("utf-8")
client_socket.send(data_to_send)
client_socket.close()
