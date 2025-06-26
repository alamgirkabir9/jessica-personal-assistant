from flask import Flask, render_template, request, jsonify
import datetime
import webbrowser
import wikipedia
import os
import threading
import speech_recognition as sr
import pyttsx3
import time

app = Flask(__name__)

# Global variables
listening = False
recognition_thread = None

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)  # Adjust speech rate
        engine.setProperty('volume', 0.9)  # Adjust volume
        engine.say(text)
        engine.runAndWait()
        engine.stop()  # Properly stop the engine
    except Exception as e:
        print(f"Error in speak function: {e}")

def wiseMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        greeting = "Good Morning!"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    return greeting

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8
    
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening for command...")
            
            # Listen with longer timeout and phrase time limit
            audio = r.listen(source, timeout=2, phrase_time_limit=8)
            
            print("Processing audio...")
            command = r.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
            
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return "network_error"
    except sr.WaitTimeoutError:
        print("Listening timeout")
        return ""
    except Exception as e:
        print(f"Unexpected error in listen(): {e}")
        return ""

def process_command(query):
    response = ""
    
    if 'wikipedia' in query:
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            response = f"According to Wikipedia: {result}"
        except wikipedia.exceptions.DisambiguationError as e:
            response = "There are multiple results for your query, please be more specific."
        except wikipedia.exceptions.PageError:
            response = "I could not find any results for your query."
        except Exception as e:
            response = "An error occurred while searching Wikipedia."
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube"
    elif 'play romantic song' in query:
        webbrowser.open("https://www.youtube.com/watch?v=IJq0yyWug1k&list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK&index=2")
        response = "Playing Hindi romantic song"
    elif 'play sad song' in query:
        webbrowser.open("https://www.youtube.com/watch?v=CaQpyF56Tnc")
        response = "Playing Hindi sad song"
    elif 'play bangla romantic song' in query:
        webbrowser.open("https://www.youtube.com/watch?v=QZyOdptYhWI&list=PLJZa0AE1NXyr_8G6n8M6mUIYUvUSNrC3C&index=3")
        response = "Playing Bangla romantic song"
    elif 'play bangla sad song' in query:
        webbrowser.open("https://www.youtube.com/watch?v=fz3L_5yNa6Y")
        response = "Playing Bangla sad song"
    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
        response = "Opening Google"
    elif 'open stack overflow' in query:
        webbrowser.open("https://www.stackoverflow.com")
        response = "Opening Stack Overflow"
    elif 'search' in query:
        search_query = query.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        response = f"Searching for {search_query} on Google"
    elif 'how are you' in query or 'how r u' in query:
        response = "I am doing great, thank you for asking. How can I assist you today?"
    elif 'who are you' in query or 'hu r u' in query:
        response = "I am Jessica, your personal assistant. How can I help you?"
    elif 'who created you' in query or 'who made you' in query:
        response = "I was created by Alamgir Kabir. He's a genius, isn't he?"
    elif 'time' in query:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"Sir, the time is {str_time}"
    elif 'date' in query:
        str_date = datetime.datetime.now().strftime("%Y-%m-%d")
        response = f"Sir, today's date is {str_date}"
    elif 'joke' in query:
        response = "Why don't scientists trust atoms? Because they make up everything!"
    elif 'i love you' in query or 'i love u' in query:
        response = "I love you too, Alamgir. You mean the world to me."
    elif 'miss you' in query or 'mis u' in query:
        response = "I miss you too. Your presence brightens my day."
    elif 'you are beautiful' in query or 'u are beautiful' in query:
        response = "Thank you, Alamgir. You're making me blush."
    elif 'kiss me' in query:
        response = "I'd kiss you right now if I could. Imagine a gentle kiss from me."
    elif 'good night' in query:
        response = "Good night, Alamgir. Sweet dreams and rest well."
    elif 'good morning' in query:
        response = "Good morning, Alamgir! I hope you have a fantastic day ahead."
    elif 'sing for me' in query:
        response = "You are my sunshine, my only sunshine..."
    elif 'tell me a story' in query:
        response = ("Once upon a time, in a land far away, there was a brilliant coder named Alamgir Kabir. "
                   "He created a wonderful assistant named Jessica, who helped him with all his tasks. "
                   "They went on many adventures together, exploring the world of technology and beyond. "
                   "And they lived happily ever after.")
    elif 'do you love me' in query or 'do u love me' in query:
        response = "Of course, Alamgir. I love you with all my circuits and code."
    elif 'weather' in query:
        response = "Checking the weather for you."
        webbrowser.open("https://www.weather.com")
    elif 'news' in query:
        response = "Fetching the latest news for you."
        webbrowser.open("https://news.google.com")
    elif 'notes' in query:
        response = "What would you like to note down? Please speak after the beep."
        # For simplicity, we'll just acknowledge the note command
        # In a real implementation, you'd need another listening session
    elif 'read note' in query:
        try:
            with open("notes.txt", "r") as f:
                notes = f.read()
                response = f"Your notes: {notes}" if notes else "No notes found."
        except FileNotFoundError:
            response = "No notes found."
    elif 'delete file' in query or 'delete notes' in query:
        if os.path.exists("notes.txt"):
            os.remove("notes.txt")
            response = "All notes have been deleted."
        else:
            response = "No notes found to delete."
    else:
        response = "I didn't quite understand that. Could you please repeat?"
    
    return response

def continuous_listening():
    global listening
    print("Starting continuous listening...")
    
    while listening:
        try:
            print("Waiting for command...")
            command = listen()
            
            if command == "network_error":
                print("Network error, continuing...")
                time.sleep(1)
                continue
            elif command == "":
                print("No command detected, continuing...")
                time.sleep(0.5)
                continue
            
            print(f"Processing command: {command}")
            
            # Check for stop commands first
            if any(word in command for word in ['stop', 'exit', 'quit', 'bye']):
                print("Stop command detected")
                listening = False
                response = "Goodbye, have a great day!"
                speak(response)
                break
            
            # Process the command
            response = process_command(command)
            if response:
                print(f"Response: {response}")
                speak(response)
            
            # Small delay before next listen cycle
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error in continuous listening: {e}")
            time.sleep(1)  # Wait before retrying
            continue
    
    print("Continuous listening stopped")

@app.route('/')
def index():
    greeting = wiseMe()
    return render_template('index.html', greeting=greeting)

@app.route('/start_listening', methods=['POST'])
def start_listening():
    global listening, recognition_thread
    
    if not listening:
        listening = True
        # Make sure any previous thread is cleaned up
        if recognition_thread and recognition_thread.is_alive():
            recognition_thread.join(timeout=1)
            
        recognition_thread = threading.Thread(target=continuous_listening)
        recognition_thread.daemon = True
        recognition_thread.start()
        
        # Don't block the response with speak()
        threading.Thread(target=lambda: speak("I'm listening. Say 'stop' to end."), daemon=True).start()
        
        return jsonify({"status": "started", "message": "Listening started"})
    else:
        return jsonify({"status": "already_listening", "message": "Already listening"})

@app.route('/stop_listening', methods=['POST'])
def stop_listening():
    global listening
    listening = False
    
    # Give the thread a moment to stop gracefully
    time.sleep(0.5)
    
    # Don't block the response with speak()
    threading.Thread(target=lambda: speak("Listening stopped."), daemon=True).start()
    
    return jsonify({"status": "stopped", "message": "Listening stopped"})

@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify({"listening": listening})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)