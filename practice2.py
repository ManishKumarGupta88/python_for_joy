#Install an external module and use it to perform an operation of your interest
#type to install "pip install pyttsx3" in terminal then run
import pyttsx3
engine=pyttsx3.init()
engine.say("hello manish how are you")
engine.runAndWait()
