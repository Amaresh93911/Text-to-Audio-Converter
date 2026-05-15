from gtts import gTTS
from playsound import playsound
audio = "speech.mp3"
language = 'en'
sp = gTTS(text=" I am amaresh",lang = language)
sp.save(audio)
playsound(audio)
print("---- audio is playing ----")
