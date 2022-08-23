import pyttsx3

text_speech = pyttsx3.init()
answer = input("What you want to convert to speech : ")
text_speech.say(answer)
text_speech.runAndWait()
text_speech.stop()
print("Done")
engine = pyttsx3.init()
engine.say("Your Input" + answer + "was Successfuly converted to speech")
engine.runAndWait()
engine.stop()