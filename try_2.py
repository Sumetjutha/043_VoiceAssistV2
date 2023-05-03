import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listener = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    
machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            print("Listening ")
            speech = listener.listen(origin)
            instruction = listener.recognize_goggle(speech)
            instruction = instruction.lower()
            if "Jarvis" in instruction:
                print(instruction)
    except:
        pass
    return instruction

def play_Jarvis():
    instruction = input_instruction
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime
        
play_Jarvis()