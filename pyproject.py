import pyttsx3 #pip install pyttsx3
import wikipedia #pip install wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
if __name__=="__main__":
    while True:
        din=input("Enter Query!!!")
        query = din.lower()
        # Logic for executing tasks based on query
        speak('Searching Wikipedia...')
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to wikipedia")
        
        print(results)
        speak(results)