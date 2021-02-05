import speech_recognition as sr

def get_text_from_speech(recognizer, microphone, language='en-US'):

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language = language)
    except sr.RequestError:
        text = "API unavailable"
    except sr.UnknownValueError:
        text = "Unable to recognize speech"

    return text

if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # set the language
    language = 'bn-BD'
    while True:
        guess = get_text_from_speech(recognizer, microphone, language)
        print(guess)
        print('Say something....')