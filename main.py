# imort speech recognition package
import speech_recognition as sr

class voiceAssistant:
    voiceText=''
    def __init__(self):
        voiceAssistant.listener(self)

    # def speaker():
    def run_operation(self):
        # check if you said "bye bye" in a few Data Model, break the loop and terminate the operation
        if(self.voiceText == "bye-bye" or  self.voiceText == "bye bye"):
            return break
    def listener(self):
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
                # try: # if your voice recognited
                    # convert the Microphone input (audio variable) to text using Google Cloud Speech API 
                text = rec.recognize_google(audio)
                # print what you said
                self.voiceText=format(text)
                print(self.voiceText)
                
                returnValue = self.run_operation()
                eval(returnValue)
                # except:
                #     # if your voice not recognited clearly
                #     print("Sorry! could not recognize your voice")

assistant = voiceAssistant()
# assistant