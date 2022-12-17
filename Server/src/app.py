import threading
import barbaros_server
import barbaros_gui
import tkinter as tk



barbaros_server.initialize_server("192.168.1.28", 6000)
receiver_thread = threading.Thread(target = barbaros_server.receive_messages)
receiver_thread.start()

win = tk.Tk()
barbaros_gui.start_gui(win)
win.mainloop()

receiver_thread.join()
