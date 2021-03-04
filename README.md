# SpeechToText

Listens for words in background and saves text to SQLite database.

Optional Flask server to view the most uttered words.

## Requirements

 - [**Python**](https://www.python.org/downloads/)
 - **[PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)** 0.2.11+ - `pip install PyAudio`
 - **[SpeechRecognition](https://github.com/Uberi/speech_recognition#readme)** - `pip install SpeechRecognition`
 - **[Flask](https://palletsprojects.com/p/flask/)** - `pip install Flask`

## Usage
Change [device_index](https://pypi.org/project/SpeechRecognition/1.0.0/#microphone-device-index-none) in main.py to your microphone device.

Run main.py

Run app.py

Speak into mic and view words at [your_ip]:5000

## Configuration
See the [SpeechRecognition docs](https://github.com/Uberi/speech_recognition#readme) and the [Reference guide](https://pypi.org/project/SpeechRecognition/1.0.0/#reference) for configuration.
