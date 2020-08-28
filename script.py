from playsound import playsound
from gtts import gTTS
import sys
import os
import time
import goslate
import speech_recognition as sr
import pyaudio
from googletrans import Translator

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

in_use = True
srinp = ""
thelang = ''
languageDict = {"french":"fr",
                "chinese":"zh-cn",
                "srilankan":"si",
                "sri lankan":"si",
                "tamil":"ta",
                "russian":"ru",
                "polish":"pl",
                "romanian":"ro",
                "dutch":"nl",
                "latin":"la",
                "japanese":"ja",
                "hindi":"hi",
                "spanish":"es",
                "german":"de",
                "greek":"el",
                "italian":"it"}

def initialise():
    global languageDict
    global thelang
    is_init = False
    speak("What language shall your voice be translated into", 'en-uk')
    retrieve()
    #print(srinp)
    for key in languageDict.keys():
        if srinp.lower() == key:
            is_init = True
            thelang = languageDict[key]
            #print(thelang)
    if is_init == False:
        speak("Please say a valid Language. Try Again", 'en-uk')
        initialise()
    else:
        speak("Okay, Setup complete, the translator is ready", 'en-uk')
        print("")
        print("")
        print("--------------------------")
        print("")
        print("")
            

def retrieve():
    global srinp
    global in_use
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print(bcolors.OKBLUE + "MICROPHONE ON:" + bcolors.ENDC + "Please Speak")                                                                                   
        audio = r.listen(source) 
    try:
        text = r.recognize_google(audio)   
        print(bcolors.WARNING + "You said :" + bcolors.ENDC +" {}".format(text))
        if text == "setup" or text == "set up":
            print("-------SETUP-------")
            speak("Returning to setup", "en")
            main()
        elif text == "goodbye" or text == "exit"or text == "leave":
            print("-------EXIT-------")
            speak("Goodbye", "en")
            in_use = False
        srinp = text
        
    except:
        print("ERROR")
        
def translate_to(inp,lang):
    global thetranslation
    text = inp
    translator = Translator()
    translatedText = translator.translate(inp,dest=lang)
    print(bcolors.HEADER + "----TRANSLATION----" + bcolors.ENDC)
    print("TRANSLATION = " + translatedText.text)
    speak(translatedText.text,lang)

def speak(temp,lang):
    voice = gTTS(text=temp, lang=lang)
    voice.save("testsound.mp3")
    print(bcolors.FAIL + "Speaking," + bcolors.ENDC + bcolors.OKGREEN + "DO NOT SPEAK" + bcolors.ENDC)
    playsound("testsound.mp3")
    time.sleep(1)
    os.remove("testsound.mp3")



def main():
    
    initialise()
    while in_use == True:
        retrieve()
        if in_use == True:
            print("")
            translate_to(srinp,thelang)
        print("")
        print("")
        print("------------------------------------------")
        print("")
        
main()


