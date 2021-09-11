from speech_analyzer import record_and_recognize_audio
from threading import Thread

class audio_ii(Thread):
    
    def __init__(self): 
        Thread.__init__(self)
        # инициализация инструментов распознавания и ввода речи
        #self.recognizer = speech_recognition.Recognizer()
        #self.microphone = speech_recognition.Microphone()
        self.cache = []
    
    def run(self):
        while True:
            # старт записи речи с последующим выводом распознанной речи 
            voice_input = record_and_recognize_audio()#self.recognizer,self.microphone)
            print("=>",voice_input)
            if voice_input!=None and voice_input!="": self.cache.append(voice_input)

    def read(self):
        if len(self.cache)>0:
            a = self.cache[0]
            del self.cache[0]
            return a
        else: return None
