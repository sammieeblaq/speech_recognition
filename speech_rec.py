import speech_recognition as sr

# Instantiating the recognizer
r = sr.Recognizer()

# Reading the audio file from harvard.wav
harvard_audio = sr.AudioFile("./harvard.wav")

with harvard_audio as source:
	try:
		audio = r.record(source)
		text = r.recognize_google(audio)
		print(f"You said: {text}")
	except:
		print("Could not recognize your voice")
	   
