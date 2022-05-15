import pyttsx3
text=pyttsx3.init()
ans=input("Enter text:")
text.say(ans)
text.runAndWait()
