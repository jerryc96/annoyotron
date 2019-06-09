from playsound import playsound
import time
import random
import subprocess
import threading
import os

minTime = 0
maxTime = 60
maxRepeat = 10
rand = random.uniform(minTime, maxTime)
threadLim = 20
sound_dir = "./sound_assets/"
soundFiles = []

for file in os.listdir(sound_dir):
    if file.endswith('.wav') or file.endswith('.mp3'):
        soundFiles.append(sound_dir + file)

class AnnoyingThread (threading.Thread):
    def __init__(self, threadID, soundFile):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.soundFile = soundFile
    def run(self):
        for i in range(int(random.uniform(1, maxRepeat))):
            time.sleep(random.uniform(minTime, maxTime))
            playsound(self.soundFile)
        # for even more continuous sound replace loop above with this
        #while True:
            #time.sleep(random.uniform(minTime, maxTime))
            #playsound(self.soundFile)
    
if __name__ == '__main__':
    while True:
        threads = list()
        for threadID in range(threadLim):
            soundFile = int(random.uniform(0, len(soundFiles)))
            thread = AnnoyingThread(threadID, soundFiles[soundFile])
            thread.start()
            threads.append(thread)
        
        for t in threads:
            t.join()