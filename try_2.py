import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as origin:
        print("Listening ")
        speech = listener.listen(origin)
        instruction = listener.recognize_goggle(speech)
        instruction = instruction.lower()
        if "Jarvis" in instruction:
            print(instruction)
        print(instruction)
        
except:
    pass