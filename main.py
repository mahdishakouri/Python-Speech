# Imort speech recognition package
import speech_recognition as sr

class voiceAssistant:
    # The "voiceText" variable used to store string of User voice (using Speech Recognition)
    voiceText=''

    # Call "listener" function
    def __init__(self):
        voiceAssistant.listener(self)

    # TODO: def speaker():

    # The function check "voiceText" and deside what Operation should be run
    def run_operation(self):
        # Check if you said "bye bye" in a few Data Model, return break
        if(self.voiceText == "bye-bye" or  self.voiceText == "bye bye"):
            return "break"

    # "listener" function that listen to Microphone and use Speech Recognition to convert it to the text
    def listener(self):
        # Create recognizer instance
        rec = sr.Recognizer()

        # Print "Say somthing:" in Terminal or CMD. You can speak when you see that text.
        print("Say something: ")

        # Infinite loop to listen
        # Press Ctrl+C or say 'bye bye' to break the loop and stop operating
        while True:
            # Use Microphone as audio source
            with sr.Microphone() as source:
                # Listen to Microphone
                audio = rec.listen(source)

                try: # If your voice recognited without any error.

                    # Convert the Microphone input (audio variable) to text using Google Cloud Speech API 
                    text = rec.recognize_google(audio)
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