import speech_recognition as sr

reconhecedor = sr.Recognizer()

with sr.Microphone() as mic:
    print("Fale algo...")
    audio = reconhecedor.listen(mic)
    print("reconhecendo... aguarde...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print(texto)
