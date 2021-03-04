import speech_recognition as sr
import sqlite3
import time

def callback(recognizer, audio):
    try:
        speech_as_text = r.recognize_google(audio)
        print(speech_as_text)
        text = speech_as_text.split()

        # connects to database
        conn = sqlite3.connect('words.db')
        c = conn.cursor()

        # gets words in database
        c.execute("SELECT word FROM words")
        words_in = c.fetchall()
        
        # checks if word already in database
        for words in text:
            if any(word[0] == words for word in words_in):
                # increase count
                c.execute("UPDATE words SET count=count+1 WHERE word=?", (words,))
            else:
                # add word
                c.execute("INSERT INTO words VALUES (?, 1)", (words,))           
        conn.commit()
        conn.close()

    except sr.UnknownValueError:
        print("_____")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# obtain audio from the microphone
r = sr.Recognizer()
r.dynamic_energy_threshold = False
mic = sr.Microphone(device_index=1) # change device_index to your device

with mic as source: 
    r.adjust_for_ambient_noise(source)

# starts listening in background
stop_listening = r.listen_in_background(mic, callback)
print("Say something!")
# we're still listening even though the main thread is blocked - loop runs for about 100000 seconds
for _ in range(100000): time.sleep(1)
# call the stop function to stop the background thread
stop_listening()
# the background thread stops soon after we call the stop function
while True: time.sleep(0.1)