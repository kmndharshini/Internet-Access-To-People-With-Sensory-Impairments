import speech_recognition as sr
import pyaudio
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            if text=="quit":
                break
        except:
            print("Sorry could not recognize what you said")