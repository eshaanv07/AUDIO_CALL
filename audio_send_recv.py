def send_chunk(chunk,sendto_sock,address):
    sendto_sock.sendto(chunk.tobytes(),address)
    
def recv_chunk(sento_sock):
    data,addr=sento_sock.recvfrom(65536)
    return data,addr