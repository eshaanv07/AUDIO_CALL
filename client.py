from audio_cap import capture_audio_chunks,SAMPLE_RATE
from audio_send_recv import send_chunk,recv_chunk
from audio_playback import start_playback_stream,queue_for_playback
import numpy as np
import socket
import threading

SENDTO_IP="192.168.88.5"
SENDTO_PORT=5800
RECV_PORT=5800

send_address=(SENDTO_IP,SENDTO_PORT)

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',RECV_PORT))

def send_loop():
    for chunk in capture_audio_chunks():
        send_chunk(chunk,sock,send_address)
        
def receive_loop():
    while True:
        chunk,addr=recv_chunk(sock)
        audio_array = np.frombuffer(chunk,dtype=np.float32).reshape(-1,1)
        queue_for_playback(audio_array)
        
if __name__ == '__main__':
    start_playback_stream()
    threading.Thread(target=receive_loop,daemon=True).start()
    send_loop()