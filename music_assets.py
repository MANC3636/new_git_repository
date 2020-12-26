from pygame import *

class Music:
    def __init__(self, music1, music2=None):
        self.music1=music1
        self.music2=music2

    def play_music(self):
        #mixer.init()
        mixer.music.load(self.music1)
        mixer.music.play(loops=-1)
        while mixer.music.get_busy():
            #continue
            time.Clock().tick(1)



