from vidstream import *
import tkinter as tk
import socket
import threading

local_ip_address = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_address, 5100)
receiver = AudioReceiver(local_ip_address, 8100)

def start_Listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
    
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), 8180)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()
    
def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 5150)
    t4 = threading.Thread(target=screen_client.start_stream) 
    t4.start()
    
def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'), 8188)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()

# GUI
window = tk.Tk()
window.title("Remote Desktop App")
window.geometry('300x300')

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Search", width=50, command=start_Listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Stream Camera", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Share Screen", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Stream Audio", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()