import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="es-ES").lower()
    except sr.UnknownValueError:
        return None
