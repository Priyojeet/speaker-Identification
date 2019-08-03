from pydub import AudioSegment
from pydub.utils import make_chunks
from ui import *
import pyaudio
import wave
import subprocess
import glob, os
import time
import threading
import pylab



v = printt()


class Recorder():
    #Defines sound properties like frequency and channels
    def __init__(self, chunk=1024, channels=2, rate=44100):
        self.CHUNK = chunk
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self._running = True
        self._frames = []

    #Start recording sound
    def start(self):
        threading._start_new_thread(self.__recording, ())

    def __recording(self):
        #Set running to True and reset previously recorded frames
        self._running = True
        self._frames = []
        #Create pyaudio instance
        p = pyaudio.PyAudio()
        #Open stream
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        # To stop the streaming, new thread has to set self._running to false
        # append frames array while recording
        while(self._running):
            data = stream.read(self.CHUNK)
            self._frames.append(data)

        # Interrupted, stop stream and close it. Terinate pyaudio process.
        stream.stop_stream()
        stream.close()
        p.terminate()

    # Sets boolean to false. New thread needed.
    def stop(self):
        self._running = False

    #Save file to filename location as a wavefront file.
    def save(self, dirpath):
        print("Saving")
        p = pyaudio.PyAudio()
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
            i = 0
            while os.path.exists(dirpath+"sample%s.wav" % i):
                i += 1

            wf = wave.open(dirpath+"sample%s.wav" % i, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self._frames))
            wf.close()
            print("Saved")
        else:
            i = 0
            while os.path.exists(dirpath+"sample%s.wav" % i):
                i += 1
            wf = wave.open(dirpath+"sample%s.wav" % i, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self._frames))
            wf.close()
            print("Saved")

def get_voiceforRegistration():    
    dirpath = "data/test_data/"+v+"/"
    rec = Recorder()
    print("Start recording")
    rec.start()
    time.sleep(90)
    print("Stop recording")
    rec.stop()
    print("Saving")
    rec.save(dirpath)

get_voiceforRegistration()
#new edition

file_name = "data/test_data/"+v+"/"

# spliting wave file

myaudio = AudioSegment.from_file(file_name+"sample0.wav" , "wav") 
chunk_length_ms = 10*1000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = file_name+"chunk{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")

def get_file(path):
    #path = 'wav_file'
    name = os.path.basename(path)
    filename, file_extension = os.path.splitext(name)
    return filename

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig(get_file(wav_file)+".png")
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

os.chdir(file_name)
for file in glob.glob("*.wav"):
    #print(file)
    graph_spectrogram(file)
    if os.path.exists(file):
        os.remove(file)
        print("file deleted")
    else:
        print("The file does not exist")

