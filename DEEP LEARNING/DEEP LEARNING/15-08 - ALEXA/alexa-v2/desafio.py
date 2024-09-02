import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import wolframalpha

# Inicializa o módulo de fala
alexa = pyttsx3.init()
alexa.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
alexa.setProperty('volume', 1.0)
alexa.setProperty('rate', 160)

# Inicializa o reconhecedor de fala
reconhecedor = sr.Recognizer()

# Função para falar
def falar(texto):
    """Fala o texto fornecido."""
    alexa.say(texto)
    alexa.runAndWait()

# Função para ouvir
def ouvir():
    """Ouvir o áudio e retornar o texto reconhecido."""
    with sr.Microphone() as mic:
        # Ajustar ao barulho do ambiente
        reconhecedor.adjust_for_ambient_noise(mic, duration=2)
        print("Estou ouvindo...")
        audio = reconhecedor.listen(mic)

        try:
            texto = reconhecedor.recognize_google(audio, language='pt')
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi. Pode repetir?")
            return None
        except sr.RequestError as e:
            print(f"Não consegui conectar ao serviço de reconhecimento de fala: {e}")
            return None

# Função para responder perguntas gerais
def responder_pergunta(pergunta):
    """Responde perguntas gerais usando o Wolfram Alpha."""
    try:
        client = wolframalpha.Client('YOUR_WOLFRAM_ALPHA_API_KEY')
        resposta = client.query(pergunta)
        resposta_formatada = next(resposta.results).text
        falar(resposta_formatada)
    except Exception as e:
        print(f"Erro ao buscar resposta: {e}")
        falar("Desculpe, não consegui encontrar uma resposta para essa pergunta.")

# Função para realizar cálculos
def calcular(texto):
    """Realiza cálculos básicos."""
    conta = texto.split()
    try:
        if conta[1] == '+':
            resultado = float(conta[0]) + float(conta[2])
        elif conta[1] == '-':
            resultado = float(conta[0]) - float(conta[2])
        elif conta[1] == 'x':
            resultado = float(conta[0]) * float(conta[2])
        elif conta[1] == '/' and float(conta[2]) != 0:
            resultado = float(conta[0]) / float(conta[2])
        else:
            falar("Não consegui entender a operação.")
            return
        falar(f"O resultado é {resultado}")
    except:
        falar("Não consegui entender a operação.")

# Loop principal
while True:
    comando = ouvir()
    if comando is not None:
        if "olá" in comando:
            falar("Olá! Como posso ajudar?")
        elif "que horas são" in comando:
            agora = datetime.datetime.now()
            falar(f"Agora são {agora.hour} horas e {agora.minute} minutos.")
        elif "quem é" in comando or "o que é" in comando:
            responder_pergunta(comando)
        elif "calcule" in comando:
            calcular(comando)
        elif "sair" in comando or "desligar" in comando:
            falar("Até mais!")
            break
        else:
            falar("Não entendi. Pode repetir?")