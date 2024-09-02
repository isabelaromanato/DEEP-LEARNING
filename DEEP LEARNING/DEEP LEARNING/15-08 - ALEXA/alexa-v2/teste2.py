import speech_recognition as sr
import pyttsx3

alexa = pyttsx3.init()

# VER QUAL A VOZ ESTÁ INSTALADA
# for voz in alexa.getProperty('voices'):
#     print(voz.id)

alexa. setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
alexa.setProperty('volume', 1.0)
alexa.setProperty('rate', 160)
reconhecedor = sr.Recognizer()

with sr.Microphone() as mic:
    # AJUSTAR AO BARULHO DO AMBIENTE
    reconhecedor.adjust_for_ambient_noise(mic, duration=2)
    print("O que deseja calcular?..")
    # ALEXA FALAR
    alexa.say('O que deseja calcular?')
    alexa.runAndWait()
    audio = reconhecedor.listen(mic)
    print("Aguarde...")
    texto = reconhecedor.recognize_google(audio, language='pt')
    print(texto)
    conta = texto.split()
    print(conta)

    resultado = None
    try:
        if conta[1] == '+':
            resultado = float(conta[0]) + float(conta[2])

        elif conta[1] == '-':
            resultado = float(conta[0]) - float(conta[2])

        elif conta[1] == 'x':
            resultado = float(conta[0]) * float(conta[2])

        elif conta[1] == '/' and  float(conta[2]) != 0:
            resultado = float(conta[0]) / float(conta[2])
    except:
        print("Nãp consegui entender!")
        alexa.say("Nãp consegui entender!")
        alexa.runAndWait()
    if resultado is not None:
        print(resultado)
        alexa.say("O resultado é " + str(resultado))
        alexa.runAndWait()