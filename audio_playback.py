import sounddevice as sd
import queue
import numpy as np

SAMPLE_RATE=44100
playback_queue=queue.Queue()

def output_callback(outdata,frames,time_info,status):
    try:
        chunk=playback_queue.get_nowait()
    except queue.Empty:
        chunk=np.zeros((frames,1),dtype='float32')
    outdata[:]=chunk

def start_playback_stream():
    stream=sd.OutputStream(samplerate=SAMPLE_RATE,channels=1,callback=output_callback)
    stream.start()
    return stream

def queue_for_playback(audio_array):
    playback_queue.put(audio_array)