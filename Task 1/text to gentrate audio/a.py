
import pyttsx3


engine = pyttsx3.init()


text = "Your are my only one. yellocard"

engine.say(text)

engine.save_to_file(text, 'output.mp3')


engine.runAndWait()

