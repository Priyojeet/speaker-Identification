from recoder import *
import glob, os
import wave
import pylab



def training():
	get_model()
	print("training complete....")


# getting the audio
def getAudio():
    rec = Recorder()
    print("Start recording")
    rec.start()
    time.sleep(11)
    print("Stop recording")
    rec.stop()
    print("Saving")
    rec.save("test.wav")
#getAudio()

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


def create_img():
	graph_spectrogram("test.wav")
	print("img creeated")


def delete_wav(file):
	if os.path.exists(file):
  		os.remove(file)
  		print("file deleted")
	else:
  		print("The file does not exist")

def delt():
	file_name = "test.wav"
	delete_wav(file_name)

