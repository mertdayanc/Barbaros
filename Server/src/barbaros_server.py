import socket
import threading
import barbaros_gui
import time

ip_address = ""
port = 0
bufferSize  = 1024
udp_socket = 0

def initialize_server(ip_addr, portNumber): # UDP Server Initialize
    # verilen ip ve port da socket aç
    global udp_socket
    global ip_address
    global port
    ip_address = ip_addr
    port = portNumber
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_socket.bind((ip_address, port))

def listen(): # Listen for message
    global bufferSize
    global udp_socket
    try:
        message = udp_socket.recvfrom(bufferSize)
    except:
        print('Closing Server')
        return 0
    return message

stop_mutex = threading.Lock()
stop_condition = False
def receive_messages():
    global stop_condition
    while True:
        stop_mutex.acquire()
        if stop_condition == True:
            stop_mutex.release()
            break
        stop_mutex.release()
        message = listen()
        if message != 0:
            barbaros_gui.on_message_received(message)

def close_server():
    global udp_socket
    global stop_condition
    stop_mutex.acquire()
    stop_condition = True
    udp_socket.close()
    stop_mutex.release()
