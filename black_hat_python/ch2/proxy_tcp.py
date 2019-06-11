#!/usr/bin/python
import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		server.bind((local_host,local_port))
	except:
		print("[!!] FAILED TO LISTEN ON %S:%D" % (local_host, local_port))
		print("[!!] CHECK FOR OTHER LISTENING SOCKETS OR CORRECT PERMISSIONS.")
		sys.exit(0)

	print("[*] Listening on %s:%d" % (local_host,local_port))
	
	server.listen(5)

	while True:
		client_socket, addr = server.accept()

		# print out the local connection information
		print("[==>] Receiving incoming ocnnection from %s:%d" % (addr[0],addr[1]))

		# start a thread to talk to the remote host
		proxy_thread = threading.Thread(target=proxy_handler,args=(client_socket,remote_host,remote_port,receive_first))

		proxy_thread.start()

def proxy_handler(client_socket,remote_host,remote_port,receive_first):
	#connect to the remote host
	remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	remote_socket.connect((remote_host,remote_port))

	# receive data from the remote end if necessary
	if receive_first:
		remote_buffer = receive_from(remote_socket)
		hexdump(remote_buffer)

		# send it to our response handler 
		remote_buffer = response_handler(remote_buffer)

		# if we have datat to send to our local client, send it
		if len(remote_buffer):
			print("[<==] Sending %d bytes to localhost" % len(remotebuffer))
			client_socket.send(remote_buffer)

	# now lets loop and reate from local
	while True:
		# read from local host
		local_buffer = receive_from(client_socket)

		if len(local_buffer):
			print("[==>] Received %d bytes from localhost." % len(local_buffer))
			hexdump(local_buffer)

			# send it to our request handler
			local_buffer = request_handler(local_buffer)

			# send off the data to the remote host
			remote_socket.send(lcoalbuffer)
			print("[==>] Sent to remote.")

		# receive back the response
		remote_buffer = receive_from(remote_socket)

		if len(remote_buffer):
			print("[<==] Received %d bytes from remote." % len(remote_buffer))
			hexdump(remote_buffer)

			# send to our response handler
			remote_buffer = response_handler(remote_buffer)

			# send the response to the local socket
			client_socket.send(remote_buffer)

			print("[<==] Sent to localhost.")
		# if no more data on either side, close the connection
		if not len(local_buffer) or not len(remote_buffer):
			client_socket.close()
			remote_socket.close()
			print("[*] No more data. Closing connection.")
			break
			
def hexdump(src, length=16):
	result = []
	digits = 4 if isinstance(src, unicode) else 2

	for i in xrange(0, len(src), length):
		s = src[i:i+length]
		hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s[)
		text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
		result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text))
	print b'\n'.join(result)

def main():
	if len(sys.argv[1:]) != 5:
		print("Usage: ./proxy_tcp.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
		print("Example: ./proxy_tcp.py 1.2.3.4 9000 1.1.1.1 9019 True")
		sys.exit(0)

	# set up local stuff
	local_host = sys.argv[1]
	local_port = int(sys.argv[2])

	# set up remote stuff
	remote_host = sys.argv[3]
	remote_port = int(sys.argv[4])

	#this tells the proxy to connect and receive data before sending to the remote host
	receive_first = sys.argv[5]

	if "True" in receive_first:
		receive_first = True
	else:
		receive_first = False

	# now spin up our listening socket
	server_loop(local_host,local_port,remote_host,remote_port,receive_first)

main()
