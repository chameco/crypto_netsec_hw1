'''
This is the server.py for the first Cryptography and Network Security I Assignment from Professor Yener.
'''
# imports. Socket for networking stuff, toy_des for encryption/decryption
import socket
import toy_des
import sys

if __name__ == "__main__":
	# users are going to send files using localhost and easy ports. This is a TCP server. 

	# credits to this for helping me set up the server https://pymotw.com/3/socket/tcp.html and https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/
	if len(sys.argv) != 3 or len(sys.argv[2]) != 10:
		print("usage: server.py \"<insert filename here>\" <10-bit key here>")

	filename = sys.argv[1]
	key = sys.argv[2]
	f = open(filename, 'r')
	entire_message = f.read() 
	# print(entire_message) to make sure it works
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# binding the server to a port 
	serv_addr = ('localhost', 9095)
	sock.bind(serv_addr)

	# encrypt the file to send upon a connection 

	# code from toy_des.py 
	secret_bin = toy_des.text_to_bits(entire_message)
	block_list = []
	block = ""
	# print(len(secret_bin))
	for i in range(0, len(secret_bin), 8):
		for j in range(i, i+8):
			if j == len(secret_bin):
				break
			block += secret_bin[j]
		block_list.append(block)
		block = ""

	Key1, Key2 = toy_des.key_getter(key)

	encrypt_list = [] 
	encrypt_string = ""
	for i in range(len(block_list)):
		encrypt_list.append(toy_des.encryptor(block_list[i], Key1, Key2))

	for i in range(len(encrypt_list)):
		encrypt_string += toy_des.text_from_bits(encrypt_list[i])

	# want to send the encrypted string 
	# listen for incoming connections 
	sock.listen(1) 
	while True: 
		try: # this will just keep sending the encrypted message 
			connection, cli_addr =  sock.accept()
			print("connection from:", cli_addr)
			print("sending the encrypt_string of the message:", encrypt_string)
			connection.sendall(encrypt_string.encode())
		finally: 
			connection.close()