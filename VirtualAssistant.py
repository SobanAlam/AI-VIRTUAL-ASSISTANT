import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

    
listener=sr.Recognizer()

machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction=" "
    try:
        with sr.Microphone() as origin:
             print("listening....")
             speech=listener.listen(origin)
             instruction=listener.recognize_google(speech)
             instruction=instruction.lower()
             if "Virtual Assistant" in instruction:
                 instruction=instruction.replace('Virtual Assistant', ' ')
                 print(instruction)
             
    
    except:
        pass
    return instruction
    
    
def play_VirtualAssistant():
    
    instruction=input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play',"")
        talk("playing"+song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time'+time)
        print(time)
         
    elif 'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date"+date)
        print(date)
        
    elif 'how are you' in instruction:
        response="I am good how about you"
        talk(response)
        print(response)
        
        
        
    elif 'What is your name' in instruction:
        response="I am Virtual Assistant What can i do for you"
        talk(response)
        print(response)
        
    elif 'open google' in instruction:
        webbrowser.open("google.com")
        
    elif 'open stack overflow' in instruction:
        webbrowser.open("stackoverflow.com")
        
    
    elif 'who is' in instruction:
        human= instruction.replace('who is'," ")
        info=wikipedia.summary(human,4)
        print(info)
        talk(info)
        
        
    
    else:
        talk("please repeat")
play_VirtualAssistant()        