import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

class VoiceAssistant:
    def __init__(self, master):
        self.master = master
        master.title("Voice Assistant")

        self.label = tk.Label(master, text="Assistant Response:")
        self.label.pack()

        self.response_box = scrolledtext.ScrolledText(master, height=5, width=50)
        self.response_box.pack()

        self.listen_button = tk.Button(master, text="Listen", command=self.listen)
        self.listen_button.pack()

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-us')
            print(f"You said: {query}\n")
            self.response_box.insert(tk.END, f"You said: {query}\n\n")
            self.handle_command(query.lower())
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            self.response_box.insert(tk.END, "Sorry, I couldn't understand what you said.\n\n")
        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition service; {e}")
            self.response_box.insert(tk.END, f"Request error from Google Speech Recognition service; {e}\n\n")

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def handle_command(self, command):
        if "hello" in command:
            self.speak("Hello! How can I help you?")
            self.response_box.insert(tk.END, "Assistant: Hello! How can I help you?\n\n")
        elif "goodbye" in command:
            self.speak("Goodbye!")
            self.response_box.insert(tk.END, "Assistant: Goodbye!\n\n")
        elif 'wikipedia' in command:
            self.speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            self.speak("According to Wikipedia")
            print(results)
            self.speak(results)

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in command:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            self.speak(f"Sir, the time is {strTime}")

        elif 'open code' in command:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
 
        else:
            self.speak("I'm sorry, I didn't understand that.")
            self.response_box.insert(tk.END, "Assistant: I'm sorry, I didn't understand that.\n\n")

def main():
    root = tk.Tk()
    assistant = VoiceAssistant(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    