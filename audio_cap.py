import sounddevice as sd
import queue

SAMPLE_RATE=44100
CHUNK_DURATION=0.01
BLOCK_SIZE=int(SAMPLE_RATE*CHUNK_DURATION)

audio_queue=queue.Queue()

def audio_callback(indata,frames,time_info,status):
    audio_queue.put(indata.copy())
    
def capture_audio_chunks():
    stream=sd.InputStream(samplerate=SAMPLE_RATE,channels=1,blocksize=BLOCK_SIZE,callback=audio_callback)
    with stream:
        while True:
            chunk=audio_queue.get()
            yield chunk

