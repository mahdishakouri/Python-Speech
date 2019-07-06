# Imort speech recognition package
import speech_recognition as sr
import pyttsx3

class voiceAssistant:
    # The "voiceText" variable used to store string of User voice (using Speech Recognition)
    voiceText=''


    # Call "listener" function
    def __init__(self):
        # Create recognizer instance
        self.rec = sr.Recognizer()

        # Create PYTTSX instance
        # Use one of the following drivers
        # sapi5 - SAPI5 on Windows
        # nsss - NSSpeechSynthesizer on Mac OS X
        # espeak - eSpeak on every other platform
        self.engine = pyttsx3.init()

        # Setting up new voice rate
        self.engine.setProperty('rate', 110)

        # Setting up volume level  between 0 and 1
        self.engine.setProperty('volume',0.9)

        # Getting details of current voice
        voices = self.engine.getProperty('voices')

        # Changing index, changes voices.
        self.engine.setProperty('voice', voices[0].id)  # o for male
        # self.engine.setProperty('voice', voices[1].id) # 1 for female

        # Say welcome
        self.speaker()

        # Call "listener" function
        self.listener()
        

    def speaker(self,text=''):
        if text=='' :
            text="Hello, Welcome to the Voice Assistant"
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()
        

    # The function check "voiceText" and deside what Operation should be run
    def run_operation(self):
        # Check if you said "bye bye" in a few Data Model, return break
        if(self.voiceText == "bye-bye" or  self.voiceText == "bye bye"):
            self.speaker("Have nice day. Good bye!")
            return "break"

    # "listener" function that listen to Microphone and use Speech Recognition to convert it to the text
    def listener(self):
        # Print "Say somthing:" in Terminal or CMD. You can speak when you see that text.
        self.speaker("Say something:")

        # Infinite loop to listen
        # Press Ctrl+C or say 'bye bye' to break the loop and stop operating
        while True:
            # Use Microphone as audio source
            with sr.Microphone() as source:
                # Listen to Microphone
                audio = self.rec.listen(source)

                try: # If your voice recognited without any error.

                    # Convert the Microphone input (audio variable) to text using Google Cloud Speech API 
                    text = self.rec.recognize_google(audio)
                    # Print what you said
                    self.voiceText=format(text)
                    print(self.voiceText)
                    
                    # Call "run_operation" function that the function will be processed your voice
                    # If you say "bye bye", the while loop will be broken and the the Voice Assistant stop working
                    if self.run_operation() == "break" :
                        break
                except:
                    # If your voice not recognited clearly
                    print("Sorry! could not recognize your voice")


# Create "voiceAssistant" instance
assistant = voiceAssistant()