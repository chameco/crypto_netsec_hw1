'''
This is the client.py for the first Cryptography and Network Security I Assignment from Professor Yener.
'''

import socket
import toy_des
import sys

if __name__ == "__main__":
	# users will connect to the server, 
	# get an encrypted message, and decrypts it 

	if len(sys.argv) != 3 or len(sys.argv[2]) != 10:
		print("usage: client.py \"<insert filename here>\" <10-bit key here>")

	# the filename is going to be the ouput file 

	file = sys.argv[1]
	key = sys.argv[2]

	K1, K2 = toy_des.key_getter(key)

	f = open(file, "w+")

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	serv_addr = ('localhost', 9095)
	sock.connect(serv_addr)

	while True: 
		encrypted = sock.recv(1024).decode()

		print("Received the message:", encrypted)

		# this is pretty much the same code from toy_des. 
		# it's just the decryption process
		decrypt_list = [] 
		encrypt_bits = toy_des.text_to_bits(encrypted)

		block = ""
		for i in range(0, len(encrypt_bits), 8):
			for j in range(i, i+8):
				# print(j)
				block += encrypt_bits[j]
			decrypt_list.append(block)
			block = ""

		decrypt_bits = [] 
		for i in range(len(decrypt_list)):
			decrypt_bits.append(toy_des.decryptor(decrypt_list[i], K1, K2))

		block = ""
		for i in range(len(decrypt_bits)):
			block += toy_des.text_from_bits(decrypt_bits[i])

		print("The decrpyted string is:", block)
		f.write(block)
		f.close()
		break