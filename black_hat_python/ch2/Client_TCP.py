#!/usr/bin/python
import socket

target = "localhost"
port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to the server
client.connect((target, port))

# send some data to server
client.send("My first TCP Client")

# receive some data from the server
response = client.recv(4096)
# Find out why the value here is 4096?

print response
