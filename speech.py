import speech_recognition as sr
import webbrowser as wb
import csv


googlechrome=wb.get('chrome')

##r2= sr.Recognizer()
##with sr.AudioFile(AUDIO_FILE) as source:
##    audio=r2.record(source)
##
##print(r2.recognize_google(audio))


personal_pronouns = ["I","You","He"]
adjectives = ["sad","angry","happy"]

sentencedata= ["I am happy","You are sad","You are happy"]





 

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    #print("Please wait. Calibrating microphone...")
    #r.adjust_for_ambient_noise(source,duration=5)
    print("Say something!")
    audio = r.listen(source)


print (r.recognize_google(audio))

try:
    if "youtube" in r.recognize_google(audio):
       googlechrome.open_new_tab("http://www.youtube.com")

    elif "Google" in r.recognize_google(audio):
        googlechrome.open_new_tab("http://www.google.com")
    else:
        print ("d")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
##

