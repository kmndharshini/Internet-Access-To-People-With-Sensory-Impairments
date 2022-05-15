import SpeechRecognition as sr
# initialize
r = sr.Recognizer()

with sr.Microphone() as source:
    # clear background noise
    r.adjust_for_ambient_noise(source, duration=0.3)
    with sr.AudioFile('a2.wav') as source:
        print("listening to audio")
        # capture the audio
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Audio:", text)
    except:
        print('Error')