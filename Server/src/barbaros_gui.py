import tkinter as tk
import barbaros_server

requests_frame = 0
confirm_frame = 0
request_row_count = 0
confirm_row_count = 0

def application_closed(win):
    barbaros_server.close_server()
    win.destroy()


def start_gui(win):
    global requests_frame
    global confirm_frame
    win.title("Barbaros")
    win.protocol('WM_DELETE_WINDOW', lambda: application_closed(win))
    win.geometry("300x500")
    requests_frame = tk.Frame(win)
    confirm_frame = tk.Frame(win)
    requests_frame.grid(row = 0, column = 0)
    confirm_frame.grid(row = 1, column = 0)

def accept(req_label, accept_button, reject_button):
    global request_row_count
    global confirm_row_count
    global confirm_frame
    request_text = req_label['text']
    req_label.grid_forget()
    accept_button.grid_forget()
    reject_button.grid_forget()
    confirmed_label = tk.Label(confirm_frame, text = request_text + " -> Accepted", bg="#12DD12")
    confirmed_label.grid(row = confirm_row_count, column = 0)
    request_row_count -= 1
    confirm_row_count += 1
    print("Accept command is sent to Raspberry Pi")

def reject(req_label, accept_button, reject_button):
    global request_row_count
    global confirm_row_count
    global confirm_frame
    req_label.grid_forget()
    request_text = req_label['text']
    accept_button.grid_forget()
    reject_button.grid_forget()
    confirmed_label = tk.Label(confirm_frame, text = request_text + " -> Rejected", bg="#DD1212")
    confirmed_label.grid(row = confirm_row_count, column = 0)
    request_row_count -= 1
    confirm_row_count += 1
    print("Reject command is sent to Raspberry Pi")

def on_message_received(message):
    global request_row_count
    received_text = message[0].decode('utf-8')
    id_str = received_text.split(';')[0].split(':')[1]
    name_str = received_text.split(';')[1].split(':')[1]
    text_to_display = id_str + ':' + name_str
    request_label = tk.Label(requests_frame, text = text_to_display)
    accept_button = tk.Button(requests_frame, text = "Accept")
    reject_button = tk.Button(requests_frame, text = "Reject")
    accept_button["command"] = lambda: accept(request_label, accept_button, reject_button)
    reject_button["command"] = lambda: reject(request_label, accept_button, reject_button)
    request_label.grid(row = request_row_count, column = 0)
    accept_button.grid(row = request_row_count, column = 1)
    reject_button.grid(row = request_row_count, column = 2)
    request_row_count += 1

