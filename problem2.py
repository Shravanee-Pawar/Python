import pyttsx3
engine = pyttsx3.init()
text = "hello ! this is a simple text to speech script."
engine.say(text)
engine.runAndWait()