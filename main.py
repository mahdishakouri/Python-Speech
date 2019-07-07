# Imort speech recognition package
import speech_recognition as sr
import pyttsx3
import os

class voiceAssistant:


    # Call "listener" function
    def __init__(self):
        # Create recognizer instance
        self.rec = sr.Recognizer()

        # Create PYTTSX instance
        # Use one of the following drivers
        # sapi5 - SAPI5 on Windows
        # nsss - NSSpeechSynthesizer on Mac OS X
        # espeak - eSpeak on every other platform
        self.pyttsxEngine = pyttsx3.init()

        # Setting up new voice rate
        self.pyttsxEngine.setProperty('rate', 130)

        # Setting up volume level  between 0 and 1
        self.pyttsxEngine.setProperty('volume',0.9)

        # Getting details of current voice
        voices = self.pyttsxEngine.getProperty('voices')

        # Changing index, changes voices.
        self.pyttsxEngine.setProperty('voice', voices[0].id)  # o for male
        # self.pyttsxEngine.setProperty('voice', voices[1].id) # 1 for female

        # Say welcome
        self.speaker()

        # Call "listener" function
        self.listener()
        

    def speaker(self,text=''):
        # In first Time, text = '' and "Speaker" says the following sentence
        if text=='' :
            text="Hello, Welcome to the Voice Assistant"

        # Print what is said
        print(text)
        self.pyttsxEngine.say(text)
        self.pyttsxEngine.runAndWait()
        

    # The function check "voiceText" and deside what Operation should be run
    def operation(self,text):
        # Check if you said "bye bye" in a few Data Model, return break
        if(text == "bye-bye" or  text == "bye bye"):
            self.speaker("Have nice day. Good bye!")
            return "break"
        else:
            # Split the text
            splitedText=text.split()
            # Delete first command
            fn = splitedText[0]
            # del splitedText[0]
            # # Join list items and create string
            # joinedText=' '.join(splitedText)

            # Make Lowercase
            fn=fn.lower()
            if fn == 'open':
                self.execute(splitedText[0])
            if fn == 'close':
                self.terminate(splitedText[0])
            

    def execute(self,program):
        # It just working on Windows
        self.speaker("Opening "+program)
        # Open program using shell command
        os.system('start '+program)

    def terminate(self,program):
        # It just working on Windows
        self.speaker("Closing "+program)
        # Close program using shell command
        os.system('taskkill /IM '+program.lower()+'.exe /F')

    # "listener" function that listen to Microphone and use Speech Recognition to convert it to the text
    def listener(self):
        # Print "Say somthing:" in Terminal or CMD. You can speak when you see that text.
        self.speaker("Say your command:")

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
                    textFormatted=format(text)
                    print(textFormatted)
                    
                    # Call "operation" function that the function will be processed your voice
                    # If you say "bye bye", the while loop will be broken and the the Voice Assistant stop working
                    if self.operation(textFormatted) == "break" :
                        break
                except:
                    # If your voice not recognited clearly
                    print("Sorry! could not recognize your voice")


# Create "voiceAssistant" instance
assistant = voiceAssistant()