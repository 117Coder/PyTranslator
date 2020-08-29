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
thelang_keyVal = ''
convo_mode = False
oppoLang = ''
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

recieveLangDict = {"french":'fr-FR',
                   "chinese":"zh-CN",
                   "srilankan":"si-LK",
                   "sri lankan":"si-LK",
                   "russian":"ru-RU",
                   "polish":"pl",
                   "romanian":"ro-RO",
                   "dutch":"dl-DL",
                   "latin":"la",
                   "japanese":"ja",
                   "hindi":"hi-IN",
                   "spanish":"es-ES",
                   "german":"de-DE",
                   "greek":"el-GR",
                   "italian":"it-IT"}









def initialise():
    global languageDict
    global thelang
    is_init = False
    global oppoLang
    global convo_mode
    speak("What language shall your voice be translated into", 'en-uk')
    retrieve('en-GB')
    #print(srinp)
    for key in languageDict.keys():
        if srinp.lower() == key:
            is_init = True
            thelang = languageDict[key]
            thelang_keyVal = key
            oppoLang = recieveLangDict[key]
            print(thelang + "   " + oppoLang)
    if is_init == False:
        speak("Please say a valid Language. Try Again", 'en-uk')
        initialise()
    else:
        speak("Okay, one last step. Would you like to enter conversation mode?", 'en-uk')
        retrieve('en-GB')
        if srinp.lower() == "yes" or srinp.lower == "okay" or srinp.lower == "sure":
            convo_mode = True
        else:
            speak("Okay then, single translation it is!", 'en-uk')
            convo_mode = False
        speak("Okay, Setup complete, the translator is ready", 'en-uk')
        print("")
        print("")
        print("--------------------------")
        print("")
        print("")
            









def retrieve(langRET):
    global srinp
    global in_use
    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print(bcolors.OKBLUE + "MICROPHONE ON:" + bcolors.ENDC + "Please Speak")
        playsound("beep.mp3")
        audio = r.listen(source) 
    try:
        #print(langRET)
        text = r.recognize_google(audio, language=langRET)
        #print("x " +r.recognize_google(audio, language='fr-FR') + " y")
        
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
        
    except Exception as e:
        print("Could not make that out, please say it louder")
        speak("Could not make that out, please say it louder", 'en')
        print(e)








        
def translate_to(inp,lang,langIN):
    global thetranslation
    text = inp
    translator = Translator()
    translatedText = translator.translate(inp,dest=lang,src=langIN)
    print(bcolors.HEADER + "----TRANSLATION----" + bcolors.ENDC)
    print("TRANSLATION = " + translatedText.text)
    speak(translatedText.text,lang)















def speak(temp, lang):
    voice = gTTS(text=temp, lang=lang)
    voice.save("voice.mp3")
    print(bcolors.FAIL + "Speaking," + bcolors.ENDC + bcolors.OKGREEN + "DO NOT SPEAK" + bcolors.ENDC)
    playsound("voice.mp3")
    time.sleep(1)
    os.remove("voice.mp3")







def prereq():
    skip = False
    speak("Hello, welcome to PyTranslator. Do you want to skip the tutorial?", "en")
    retrieve('en-gb')
    if srinp.lower() == "yes" or srinp.lower() == "okay" or  srinp.lower() == "sure" or  srinp.lower() == "please":
        skip = True
        initialise()
    else:
        speak("Okay, welcome to PyTranslator", "en")
        speak("This is a tool for translation, you can translate in a conversation, between english and another language, or single translation", "en")
        speak("To use this tool properly, remember, only speak after you hear a beep, that means your microphone is ready", "en")
        speak("If you are in conversation mode, the microphone alternates between english and your other language", "en")
        speak("Supported languages include:", "en")
        speak("Frech, Chinese, Sri Lankan, Tamil, Russian, Polish, Romanian, Dutch, Latin, Japanese, Hindi, Spanish, German, Greek, Italian", "en")
        speak("If you would like to review this list, you can do so on GitHub", "en")
        speak("At any time, if you would like to return to setup, to change language or mode, say. setup. when the microphone is receiving english", "en")
        speak("To leave the translator, say leave, or exit in english", "en")
        speak("Tutorial complete! Beginning setup...", "en")
        initialise()









def main():
    
    initialise()
    print("--------------LANGUAGE1 enGB-----------------")
    print("")
    if convo_mode == True:
        while in_use == True:
            retrieve('en-GB')
            if in_use == True:
                print("")
                translate_to(srinp,thelang,'en')
            print("")
            print("--------------LANGUAGE2-----------------")
            print("")
            if in_use == True:
                retrieve(oppoLang)
            if in_use == True:
                translate_to(srinp,'en',thelang)
            print("")
            print("")
            print("--------------LANGUAGE1 enGB-----------------")
            print("")
    elif convo_mode == False:
        while in_use == True:
            retrieve('en-GB')
            if in_use == True:
                print("")
                translate_to(srinp,thelang,'en')
        print("")
        print("")
        print("-------------------------------")
        print("")




        
main()
#initialise()
#retrieve('hi-IN')




