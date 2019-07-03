# imort speech recognition package
import speech_recognition as sr

# create recognizer instance
rec = sr.Recognizer()

print("Say something: ")

# Infinite loop to listen
# press Ctrl+C or say 'bye bye' to break the loop and stop operating
while True:
    # use Microphone as audio source
    with sr.Microphone() as source:
        # listen to Microphone
        audio = rec.listen(source)
        # convert the Microphone input (audio variable) to text using Google Cloud Speech API 
        text = rec.recognize_google(audio)
        # print what you said
        print("{}".format(text))
        # check if you said "bye bye" in a few Data Model, break the loop and terminate the operation
        if(format(text) == "bye-bye" or  format(text) == "bye bye"):
            break
